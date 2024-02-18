from sismic.io import import_from_yaml, export_to_plantuml
from sismic.model import Statechart, Transition
from sismic.interpreter import Interpreter
from sismic.model import Statechart, Transition, CompoundState, BasicState, FinalState
from extend import extend
import asyncio

# Load statechart from yaml file




# elevator = import_from_yaml(filepath='sismic/docs/examples/elevator/elevator.yaml')
# print(elevator._parent)


# # Create an interpreter for this statechart
# interpreter = Interpreter(elevator)

# active_state_before_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# all_events_for_the_current_state = elevator.events_for(interpreter.configuration)

# #-----REMOVE STATE -----------------------

# interpreter.queue('floorSelected', floor=7) #-----> from current level 0 I want to go level 7

# elevator.remove_state('doorsClosed')

# # interpreter = Interpreter(elevator)


# # interpreter.execute_once()

# after_confg = interpreter.configuration


# plantuml_data = export_to_plantuml(elevator)
# with open('statechart.plantuml', 'w') as file:
#     file.write(plantuml_data)

# print(after_confg)

# all_events_before = elevator.events_for(interpreter.configuration)

# # interpreter.queue('floorSelected', floor=1)



# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()
# interpreter.execute_once()

# after_confg = interpreter.configuration

# print("Ending ....")

# print('Current floor is', interpreter.context['current'])

# # current_state = interpreter.context['current']

# # current_state


# #---------ADD TRANSITION-----------------

# t1 = Transition(source = 'doorsClosed', target= 'movingDown', event='emergency')

# elevator.add_transition(t1)

# last_confg = interpreter.configuration

# plantuml_data = export_to_plantuml(elevator)
# with open('statechart.plantuml', 'w') as file:
#     file.write(plantuml_data)

# print(last_confg)

# print('XXXXXX')





##--------experiment with the testing the framework ---- composite.yaml 

# simple_sc = import_from_yaml(filepath='sismic/tests/yaml/composite.yaml')

# plantuml_data = export_to_plantuml(simple_sc)
# with open('test_composite.plantuml', 'w') as file:
#     file.write(plantuml_data)

# import json 
# import yaml
# with open('sismic/tests/yaml/composite.yaml', 'r') as yaml_file:
#     yaml_content = yaml.safe_load(yaml_file)
# json_content = json.dumps(yaml_content, indent=4)

# with open('compound_state_chart.json', 'w') as json_file:
#     json_file.write(json_content)



# interpreter = Interpreter(simple_sc)

# active_state_before_execution = interpreter.configuration

# step = interpreter.execute_once()

# interpreter.queue('click', 'close', 'validate')

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()


#--------------XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-------------------
# actions.yaml 


# simple_sc = import_from_yaml(filepath='sismic/tests/yaml/actions.yaml')

# plantuml_data = export_to_plantuml(simple_sc)
# with open('test_actions.plantuml', 'w') as file:
#     file.write(plantuml_data)


# # Create an interpreter for this statechart
# interpreter = Interpreter(simple_sc)

# active_state_before_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration



# deep_history.yaml 


# simple_sc = import_from_yaml(filepath='sismic/tests/yaml/final.yaml')

# plantuml_data = export_to_plantuml(simple_sc)
# with open('test_final.plantuml', 'w') as file:
#     file.write(plantuml_data)


# # Create an interpreter for this statechart
# interpreter = Interpreter(simple_sc)

# active_state_before_execution = interpreter.configuration

# step = interpreter.execute_once()

# interpreter.queue('parallel', 'c', 'root-final', 'parallel', 'p2-final', 'p1-final')

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration


#-----

# simple_sc = import_from_yaml(filepath='sismic/tests/yaml/nested_parallel.yaml')

# plantuml_data = export_to_plantuml(simple_sc)
# with open('test_nested_parallel.plantuml', 'w') as file:
#     file.write(plantuml_data)


# # Create an interpreter for this statechart
# interpreter = Interpreter(simple_sc)

# active_state_before_execution = interpreter.configuration

# step = interpreter.execute_once()

# interpreter.queue('parallel', 'c', 'root-final', 'parallel', 'p2-final', 'p1-final')

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration

# step = interpreter.execute_once()

# active_state_after_execution = interpreter.configuration




#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
# producer 
async def fetch_change(queue):
    
    # we have state / transition addition remove
    # lis_of_change = list()
    while(True):
        print("if no change is needed type Exit\n")
        change_or_continue = input("?: \n")
        if change_or_continue == "Exit":
            await queue.put(None)
            break
        else:
            print("insert 1 for state addition \n insert 2 for state removal \n insert 3 for transition addition \n insert 4 for transition removal \n insert 5 for Add events\n")
            in_type = input("change type: \n")
            if in_type == "1":
                print("input state type 'B' -- Basic, 'C' -- Compound, 'F' -- Final\n")
                state_type = input("state_type: \n")
                state_name = input("state_name: \n")
                on_entry = input("on_entry: \n")
                if on_entry == '':
                    on_entry = None
                on_exit = input("on_exit: \n")
                if on_exit == '':
                    on_exit = None
                parent = input("parent: \n")
                if parent == '':
                    parent = None
                initial = input("initial: \n")
                if initial == '':
                    initial = None

                state_dic = {
                    "change_type": in_type,
                    "state_type": state_type,
                    "state_name":state_name,
                    "on_entry":on_entry,
                    "on_exit":on_exit,
                    "parent":parent,
                    "initial":initial,
                } 

                await queue.put(state_dic)

            if in_type == "2":
                state_name = input("state_name: \n")

                state_dic = {
            "change_type": in_type,
            "state_name":state_name,
                }

                await queue.put(state_dic)





            if in_type == '3' or in_type == '4':
                source = input("source: \n")
                target = input("target: \n")
                event = input("event: \n")
                if event == '':
                    event = None
                guard = input("guard: \n")
                if guard == '':
                    guard = None
                action = input("action: \n")
                if action == '':
                    action = None
                priority = input("priority: \n")
                if priority == '':
                    priority = None


                tran_dic = {
                    "change_type": in_type,
                    "source": source,
                    "target":target,
                    "event":event,
                    "guard":guard,
                    "action":action,
                    "priority":priority,
                } 

                await queue.put(tran_dic)

            # Add events 
            if in_type == '5':
                num_of_events = input("How many events you want to insert?\n")
                lis_of_events = list()
                for i in range(int(num_of_events)):
                    event_name = input("insert name of the event\n")
                    lis_of_events.append(event_name)

                tran_dic = {
                    "change_type": in_type,
                    "event_list": lis_of_events,
                } 

                await queue.put(tran_dic)

                



        print("produced ....\n")



# consumer 
async def run_statechart(queue):
    

    #elevator = import_from_yaml(filepath='sismic/docs/examples/elevator/elevator.yaml')
    # ---------------------------------------------------->
    elevator = import_from_yaml(filepath='sismic/tests/yaml/simple.yaml')
    print(elevator._parent)


    # Create an interpreter for this statechart
    interpreter = Interpreter(elevator)

    active_state_before_execution = interpreter.configuration

    step = interpreter.execute_once()
    # ---------------------------------------------------->
    # interpreter.queue('floorSelected', floor=16)
    # interpreter.queue('click', 'validate') # ----> replacement 
    
    while True:
        run_again = input("Run next step ? if no type Exit: \n")
        if run_again == "Exit":
            break
        await asyncio.sleep(4)
        while True:
            if queue.empty():
                await fetch_change(queue)
                item = await queue.get()
                
            else:
                item = await queue.get()
            

            if item is None:
                # queue.task_done()
                break  # End when the sentinel value is seen

            st_change = extend.StateChange(elevator, interpreter)
            tc_change = extend.TransitionChange(elevator, interpreter)
            
            c_type = item["change_type"]
            if c_type == "1":
                s_type = item["state_type"]
                s_name = item["state_name"]
                s_on_entry = item["on_entry"]
                s_on_exit = item["on_exit"]
                s_parent = item["parent"]
                s_initial = item["initial"]

                if s_type == "B":
                    s1 = BasicState(s_name, s_on_entry, s_on_exit)
                    st_change.add(s1, s_parent)
                if s_type == "C":
                    s1 = CompoundState(s_name, s_initial, s_on_entry, s_on_exit)   
                    st_change.add(s1, s_parent)
                if s_type == "F":
                    s1 = FinalState(s_name, s_on_entry, s_on_exit)
                    st_change.add(s1, s_parent) 

            if c_type == "2":
                s_name = item["state_name"]
                st_change.remove(s_name)

            if c_type == "3" or c_type == "4":
                source = item["source"]
                target = item["target"]
                event = item["event"]
                guard = item["guard"]
                action = item["action"]
                priority = item["priority"]
                if priority!= None:
                    priority = int(priority)
                t2 = Transition(source, target, event, guard, action, priority)
                if c_type == "3":
                    tc_change.add(t2)
                if c_type == "4":
                    tc_change.remove(t2)

            if c_type == "5":
                event_list = item["event_list"]

                for event in event_list:
                    interpreter.queue(event)

            print(f"Consumed {item} \n")
            # queue.task_done()

        # print("running the step...\n")
        # active_state_after_execution = interpreter.configuration
        # print("active states before execution: \n")
        # print(active_state_after_execution)
        print(elevator.events_for(interpreter.configuration))
        step = interpreter.execute_once()
        # print("active states after execution: \n")
        # print(active_state_after_execution)
        # print(elevator.events_for(interpreter.configuration))
        


    # s1 = BasicState('Emergency')
    # s2 = FinalState('Exit')

    # st_change.add(s1, 'movingElevator')
    # st_change.add(s2, 'movingElevator')

    # t2 = Transition('doorsClosed', 'Emergency', None, 'current > 10', None, 1)
    # t3 = Transition('Emergency', 'Exit', 'leave')

    # tc_change.add(t2)
    # tc_change.add(t3)




    # for i in range(10):
    #     step = interpreter.execute_once()







    # for i in range(10):
    #     step = interpreter.execute_once()
    #     active_state_before_execution = interpreter.configuration

    # step = interpreter.execute_once()
    print("... creating PlantUML\n")
    plantuml_data = export_to_plantuml(elevator)
    with open('chapter_7/statechart_xx.plantuml', 'w') as file:
        file.write(plantuml_data)




async def main():
    queue = asyncio.Queue()
    
    task1 = asyncio.create_task(run_statechart(queue)) # consumer 
    task2 = asyncio.create_task(fetch_change(queue)) # producer 
    
    await asyncio.gather(task1, task2)

    

asyncio.run(main())

    



    








