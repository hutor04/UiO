import re
from intentions_parser import IntentionsParser


class Processor:
    def __init__(self, output_callback, action_callback, stop_callback, current_floor_cb):
        self.output_callback = output_callback
        self.action_callback = action_callback
        self.stop_callback = stop_callback
        self.current_floor_cb = current_floor_cb

        self.intention_parser = IntentionsParser()

        self.floor_regex = {
                1: r'\b(1|one|first)\b',
                2: r'\b(2|two|second)\b',
                3: r'\b(3|three|third)\b',
                4: r'\b(4|four|fourth)\b',
                5: r'\b(5|five|fifth)\b',
                6: r'\b(6|six|sixth)\b',
                7: r'\b(7|seven|seventh)\b',
                8: r'\b(8|eight|eights)\b',
                9: r'\b(9|nine|nineth)\b',
                10: r'\b(10|ten|tenth)\b'
        }

        self.name_regex = {
            'Pierre Lison': 'pierre lison',
            'Jan Tore Lønning': 'jan tore lønning',
            'Stephan Oepen': 'stephan oepen',
            'Erik Velldal': 'erik velldal',
            'Lilja Øvrelid': 'lilja øvrelid',
        }

        self.floor_mapping = {
            'Pierre Lison': 4,
            'Jan Tore Lønning': 5,
            'Stephan Oepen': 4,
            'Erik Velldal': 5,
            'Lilja Øvrelid': 4,
        }

        self.intentions = {
            1: {'name': 'Go to floor number N', 'action': self._go_to_floor_handler},
            2: {'name': 'N floors up', 'action': self._go_up_handler},
            3: {'name': 'N floors down', 'action': self._go_down_handler},
            4: {'name': 'Request current floor', 'action': self._curr_floor_request_handler},
            5: {'name': 'Request office location', 'action': self._request_office_info_handler},
            6: {'name': 'Positive answer.', 'action':  self._assertion_handler},
            7: {'name': 'Negative answer.', 'action': self._negation_handler},
            8: {'name': 'Stop action', 'action': self._stop_handler}
        }

        self.response_templates = {
            'greeting': 'Hello, I am talking elevator. Which floor to you want to go to?',
            'repeat_request': 'Can you repeat your request, please?',
            'positive_grounding': 'Ok, I understand.',
            'elevated_request': 'Please, say to which floor you want to go?',
            'stop': 'Elevator stopped upon request.',
            'min_floor': 'First, floor is the lowest floor.',
            'max_floor': 'Tenth, floor is the highest floor.',
            'going_to': 'Ok! Going to {{}} floor.',
            'curr_floor': 'You are on floor number {{}}.',
            'office_info': "{{}}'s office is on floor {{}}.",
            'additional_request': 'Do you want to go there?'
        }

        self.state = {
            'greeting': -1,
            'target_floor': -1,
            'next': {},
            'failed_requests': 0
        }
        self.greeting()

    def _reset_state(self, curr_floor=1) -> None:
        self.state['target_floor'] = -1
        self.state['next'] = {}
        self.state['failed_requests'] = 0

    def _get_state(self) -> dict:
        return self.state

    def _update_state(self, key: str, val) -> dict:
        self.state[key] = val
        return self.state

    def _normalize_user_input(self, user_input: str) -> str:
        return user_input.lower()

    def _parse_user_intention(self, user_input: str) -> int:
        intention_id = self.intention_parser.predict(user_input)
        return intention_id

    def _parse_pattern(self, pattern: dict, user_input: str) -> int:
        result = -1
        for key, regex in pattern.items():
            match = re.search(regex, user_input)
            if match is not None:
                result = key
                break
        return result

    def _respond(self, template: str, values=()) -> None:
        response = template
        for value in values:
            response = response.replace('{{}}', value, 1)
        self.output_callback(response)

    def _assertion_handler(self):
        pass

    def _negation_handler(self, user_input=''):
        self._respond(self.response_templates['positive_grounding'])
        self._respond(self.response_templates['elevated_request'])
        self._reset_state()

    def _stop_handler(self, user_input=''):
        self.stop_callback()
        self._reset_state()
        self._respond(self.response_templates['stop'])
        self._respond(self.response_templates['elevated_request'])

    def _fail_handler(self):
        curr_state = self._get_state()
        current_floor = self.current_floor_cb
        if curr_state['failed_requests'] == 3:
            self._respond(self.response_templates['elevated_request'])
            self._reset_state(curr_floor=current_floor)
        else:
            self._update_state('failed_requests', curr_state['failed_requests'] + 1)
            self._respond(self.response_templates['repeat_request'])

    def _go_to_floor(self, n: int) -> None:
        self._respond(self.response_templates['going_to'], [str(n)])
        self._update_state('target_floor', n)
        next_action = {
            7: lambda: self._stop_handler(),
            8: lambda: self._stop_handler()
        }
        self._update_state('next', next_action)
        self.action_callback(n)

    def _go_to_floor_handler(self, user_input: str) -> None:
        next_floor = self._parse_pattern(self.floor_regex, user_input)
        if next_floor != -1:
            self._go_to_floor(next_floor)
            self._update_state('failed_requests', 0)
        else:
            self._fail_handler()

    def _go_down_handler(self, user_input: str) -> None:
        current_floor = self.current_floor_cb()
        delta = self._parse_pattern(self.floor_regex, user_input)
        if delta != -1:
            if current_floor - delta < 1:
                self._respond(self.response_templates['min_floor'])
                self._update_state('failed_requests', 0)
            else:
                self._go_to_floor(current_floor - delta)
                self._update_state('failed_requests', 0)
        else:
            self._fail_handler()

    def _go_up_handler(self, user_input: str) -> None:
        current_floor = self.current_floor_cb()
        delta = self._parse_pattern(self.floor_regex, user_input)
        if delta != -1:
            if current_floor + delta > 10:
                self._respond(self.response_templates['max_floor'])
                self._update_state('failed_requests', 0)
            else:
                self._go_to_floor(current_floor + delta)
                self._update_state('failed_requests', 0)
        else:
            self._fail_handler()

    def _curr_floor_request_handler(self, user_input='') -> None:
        curr_floor = self.current_floor_cb()
        self._respond(self.response_templates['curr_floor'], (str(curr_floor)))

    def _request_office_info_handler(self, user_input: str) -> None:
        user_id = self._parse_pattern(self.name_regex, user_input)
        if user_id != -1:
            target_floor = self.floor_mapping[user_id]
            self._respond(self.response_templates['office_info'], (user_id, str(target_floor)))
            self._respond(self.response_templates['additional_request'])
            self._update_state('failed_requests', 0)
            next_action = {
                6: lambda: self._go_to_floor(target_floor),
                7: lambda: self._negation_handler(),
                8: lambda: self._stop_handler()
            }
            self._update_state('next', next_action)
        else:
            self._fail_handler()

    def greeting(self) -> None:
        current_state = self._get_state()
        if current_state['greeting'] == -1:
            self._update_state('greeting', 1)
            self._respond(self.response_templates['greeting'])
        else:
            pass

    def dispatcher(self, user_input: str, confidence_score: float) -> None:
        if confidence_score < 0.7:
            self._fail_handler()
        else:
            current_state = self._get_state()
            normalized_input = self._normalize_user_input(user_input)
            intention_id = self._parse_user_intention(normalized_input)
            if intention_id in current_state['next'].keys():
                current_state['next'][intention_id]()
                self._reset_state()
            else:
                self.intentions[intention_id]['action'](normalized_input)
            print(f'Current intention: {self.intentions[intention_id]["name"]}')



if __name__ == '__main__':
    p = Processor(print, print, print, print)
    i = p._respond(p.response_templates['office_info'], ('Pierre', '4'))
    print(i)
