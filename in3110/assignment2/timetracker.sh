#!/bin/bash

export LOGFILE=$(pwd)"/timetracker.log"
no_task="No tasks"
task_running="There is an active task running. Stop it to start a new task."
failed_stop="Nothing to stop, start a task first."
ACTIVE=$no_task
regex_start="START (.*)"
regex_label="LABEL (.*)"
regex_end="END (.*)"

function track {    
    option=$1;
    shift;
    case "$option" in
        start)
            if [ "$ACTIVE" == "$no_task" ]; then  
                task_name=$*
                if [ "$task_name" != "" ]; then
		ACTIVE=$task_name
                start_time_stamp=$( date )
                cat >> $LOGFILE <<EOF
START $start_time_stamp
LABEL $task_name
EOF
		else
		echo "Provide the name of the task."
		fi
            else
                echo $task_running
            fi

            ;;
        stop)
            if [ "$ACTIVE" == "$no_task" ]; then
                echo $failed_stop
            else
                ACTIVE=$no_task
                end_time_stamp=$( date )
                cat >> $LOGFILE <<EOF
END $end_time_stamp

EOF
            fi
            ;;

        status)
            echo $ACTIVE" in progress"
            ;;
        
        log)
            if test -f "$LOGFILE"; then
            	while IFS= read -r line
            	do
            	if [[ $line =~ $regex_start ]]; then
                	start="${BASH_REMATCH[1]}"

            	elif [[ $line =~ $regex_label ]]; then
                	label="${BASH_REMATCH[1]}"

            	elif [[ $line =~ $regex_end ]]; then
                	end="${BASH_REMATCH[1]}"

                	start_seconds=$(date -d "$start" +%s)
                	end_seconds=$(date -d "$end" +%s)
                	result=$(( (end_seconds-start_seconds) ))
                	((h=${result}/3600))
                	((m=(${result}%3600)/60))
                	((s=${result}%60))
                	printf "%s: %02d:%02d:%02d\n" "$label" $h $m $s
            		fi
            		done < "$LOGFILE"
		else
			echo "No tasks have been logged."
		fi
            ;;
        
        *)
            echo "Wrong command"
            echo "track start [label]: Starts a new task with a label"
            echo "track stop: Stops the current task, if there is one running"
            echo "track status: Tells us what task we are currently tracking"
            ;;


    esac

}
