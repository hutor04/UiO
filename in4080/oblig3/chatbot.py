import os, random, gzip, json, re, itertools, string, pickle
import tensorflow as tf
import tensorflow.keras as keras
import encoder_client
import numpy as np

DIALOGUE_FILE = "data/en-comedy.txt.gz"
FIRST_NAMES = "data/first_names.json"
MODEL_URI = "https://nr.no/~plison/data/model.tar.gz"


class Chatbot:
    def __init__(self, dialogue_data=DIALOGUE_FILE, use_pickle=True):

        # Extracts the (context, response) pairs
        self.pairs = Chatbot._load_data('data/pairs.dat') if use_pickle else self._extract_pairs(dialogue_data)

        # Loads the ConveRT utterance encoder
        self.client = encoder_client.EncoderClient(MODEL_URI)

        # Compute the embeddings for the responses (takes some time to compute!)
        responses = [response for _, response in self.pairs]
        self.response_embeddings = Chatbot._load_data('data/response_embeddings_tuned.dat') if use_pickle else \
            self.client.encode_responses(responses)

        contexts = [context for context, _ in self.pairs]
        self.context_embeddings = Chatbot._load_data('data/context_embeddings.dat') if use_pickle else \
            self.client.encode_responses(contexts)

    @staticmethod
    def _save_data(data, path):
        with open(path, 'wb') as f:
            pickle.dump(data, f)

    @staticmethod
    def _load_data(path):
        with open(path, 'rb') as f:
            result = pickle.load(f)
            return result

    def _validate_non_alpha(self, line1, line2):
        regexp = re.compile(r'[(){\[\]\}:;\"]')
        l1 = regexp.search(line1) is None
        l2 = regexp.search(line2) is None
        return l1 and l2

    def _validate_uppercase(self, line1, line2):
        return (not line1.isupper() and not line2.isupper())

    def _validate_length(self, line1, line2):
        l1 = len(line1.split(' ')) < 11
        l2 = len(line2.split(' ')) < 11
        return l1 and l2

    def _validate_names(self, line1, line2):
        l1 = line1.translate(str.maketrans('', '', string.punctuation))
        l2 = line2.translate(str.maketrans('', '', string.punctuation))

        l1 = l1.split(' ')
        l2 = l2.split(' ')

        result = True

        with open(FIRST_NAMES) as f:
            names_list = set(json.load(f))
            for line in l1:
                if line in names_list:
                    result = False
                    break
            if result:
                for line in l2:
                    if line in names_list:
                        result = False
                        break
        return result

    def _validate_pairs(self, line1, line2):
        validators = [self._validate_non_alpha, self._validate_uppercase, self._validate_length, self._validate_names]
        result = True
        for validator in validators:
            current_result = validator(line1, line2)
            if not current_result:
                result = False
        return result

    def _extract_pairs(self, dialogue_data, max_nb_pairs=100000):
        result = []
        counter = 0
        with gzip.open(dialogue_data, 'rt') as input_data:
            films = (group for k, group in itertools.groupby(input_data, key=lambda x: x.startswith("###")) if not k)
            for film in films:
                for line1, line2 in zip(film, film):
                    if counter == max_nb_pairs:
                        break
                    l1 = line1.strip()
                    l2 = line2.strip()
                    valid = self._validate_pairs(l1, l2)
                    if valid:
                        result.append([l1, l2])
                        counter += 1
        return result

    def get_response(self, user_utterance):
        encoded_utterance = self.client.encode_responses([user_utterance])
        cos_sim = np.dot(self.response_embeddings, encoded_utterance.T)
        response = np.argmax(cos_sim[:, 0], axis=0)
        return self.pairs[response][1]

    def fine_tune(self):
        # Extract the training data (with both positive and negative examples)
        context_embeddings2, response_embeddings2, outputs = self._get_training_data()

        # Creates the two input layers (for the two embeddings)
        input1 = tf.keras.layers.Input((context_embeddings2.shape[1],))
        input2 = tf.keras.layers.Input((response_embeddings2.shape[1],))

        # Computes the transformation of the response embeddings
        dense2 = tf.keras.layers.Dense(response_embeddings2.shape[1], activation="relu")

        # Computes the dot product, and pass through a sigmoid to get a probability
        dotproduct = tf.keras.layers.Dot(axes=1)
        sigmoid = tf.keras.layers.Activation(tf.keras.activations.sigmoid)

        # Connects together all layers
        output_prob = sigmoid(dotproduct([input1, dense2(input2)]))

        # Creates a new model, specifying the inputs and output
        model = tf.keras.Model([input1, input2], output_prob)
        model.summary()

        # Compile the model the "Adam" optimiser and a cross-entropy loss
        model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy'])

        # Train the model on 10 epochs
        model.fit([context_embeddings2, response_embeddings2], outputs,
                  batch_size=32, epochs=10)

        # Once the model is trained, we simple transform the response embeddings using
        # the transformation we have learned
        embeddings_tensor = dense2(self.response_embeddings)
        self.response_embeddings = tf.keras.backend.eval(embeddings_tensor)
        Chatbot._save_data(self.response_embeddings, 'data/response_embeddings_tuned.dat')

    def _get_training_data(self):
        number_samples = self.response_embeddings.shape[0]

        idx1 = np.random.randint(number_samples, size=number_samples)
        idx1_1 = np.arange(number_samples)
        idx1 = np.where(idx1 == idx1_1, np.random.randint(number_samples, size=1), idx1)

        outputs = np.ones(number_samples, dtype=int)
        neg_outputs = np.zeros(number_samples, dtype=int)

        contexts = np.concatenate((self.context_embeddings, self.context_embeddings))
        responses = np.concatenate((self.response_embeddings, self.response_embeddings[idx1, :]))
        outputs = np.concatenate((outputs, neg_outputs))

        idx2 = np.arange(contexts.shape[0])
        np.random.shuffle(idx2)

        return contexts[idx2, :], responses[idx2, :], outputs[idx2]
