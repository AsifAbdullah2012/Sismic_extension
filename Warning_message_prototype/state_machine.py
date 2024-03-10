# state_machine/state_machine.py

import json
from sismic.io import import_from_yaml
from sismic.io import export_to_plantuml
import copy
from validation import Validation
import networkx as nx
import matplotlib.pyplot as plt
import os 

class StateMachine:
    def __init__(self, state_chart):
        self.states = {state['name']: state for state in state_chart['states']}
        self.current_state_name = "root"

    # this function take even then if logical execute the event and change the current state 
    # and print the transition 
    def send_event(self, event):
        state = self.states[self.current_state_name]
        for transition in state.get('transitions', []):
            if transition['event'] == event:
                self.current_state_name = transition['target']
                return f"Transitioned to {self.current_state_name} on event '{event}'"
        return f"No transition on event '{event}' from state {self.current_state_name}"

    def get_all_variables(self):
        return vars(self)

    # draw palnt UML using the sismic library
    def draw_plant_UML(self):
        # to be done 1. read json 2. convert it to yml 3. use yml to draw 
        # -----------------from yaml file ---------------------
        # statechart_sismic = import_from_yaml('state_chart_sismic.yaml')
        # plantuml_code = export_to_plantuml(statechart_sismic)
        # with open('my_statechart.puml', 'w') as f:
        #     f.write(plantuml_code)
        if os.path.exists('plots/inspect_graph.pdf'):
            os.remove('plots/inspect_graph.pdf')
        validate = Validation(self.states)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()

        # Specify the layout for nodes 
        pos = nx.spring_layout(validation_bfs)

        # Draw the graph
        nx.draw(validation_bfs, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_weight='bold')

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(validation_bfs, 'label')
        nx.draw_networkx_edge_labels(validation_bfs, pos, edge_labels=edge_labels)
        plt.ion()  
        # Show the plot
        plt.show()
        plt.savefig('plots/inspect_graph.pdf', format='pdf')

    def add_state(self, copy_state):
        print("now we have the following states please select the name->id->transitions of the new state \n")
        print(copy_state.keys)
        name_new_state = input("name: \n")
        id_new_state = input("id: # each states must have different id\n")
        in_tran = input("How many incoming transaction\n")
        out_tran = input("How many outgoing transaction\n")
        for i in range(int(in_tran)):
            print("From which state the transaction is coming \n")
            in_tran_name = input("name: \n")
            print("What kind of event: \n")
            in_event_name = input("event: \n")
            new_transition = {"event": in_event_name, "source": "", "target": name_new_state}
            print("---->in coming transaction: \n")
            for key in copy_state:
                if key == in_tran_name:
                    temp_dic = copy_state[key]
                    temp_dic["transitions"].append(new_transition)
                    print(copy_state)
                    break

        for i in range(int(out_tran)):
            print("------>outgoing transaction: \n")
            if name_new_state not in copy_state:
                out_tran_name = input("name: ")
                out_event_name = input("outevent: ")
                temp_dic = {"id": id_new_state, "name": name_new_state, "transitions": []}
                temp_tran_dic = {"event": out_event_name, "Source": "", "target": out_tran_name}
                temp_dic["transitions"].append(temp_tran_dic)
                copy_state[name_new_state] = temp_dic
                print(copy_state)
            else:
                out_tran_name = input("name: ")
                out_event_name = input("outevent: ")
                temp_tran_dic = {"event": out_event_name, "Source": "", "target": out_tran_name}
                copy_state[name_new_state]['transitions'].append(temp_tran_dic)
                print(copy_state)


        if in_tran == "0" and out_tran == "0":
            print("both are zero ... ")
            temp_dic = {"id": id_new_state, "name": name_new_state, "transitions": [{}]}
            copy_state[name_new_state] = temp_dic

        # validation check here ...
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        valid = validate.validation_check(validation_bfs, self.current_state_name, node_lis, name_new_state)
        return valid, copy_state

    def remove_state(self, copy_state):
        print("which State you want to remove ?\n")
        name_state_remv = input("name\n")
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        in_coming_nodes = [n for n in reverse_graph.neighbors(name_state_remv)]
        for node in in_coming_nodes:
            copy_state[node]["transitions"] = [transition for transition in copy_state[node].get("transitions", []) if transition.get("target") != name_state_remv]

        del copy_state[name_state_remv]

        # validation check 
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        valid = validate.validation_check(validation_bfs, self.current_state_name, node_lis, "")

        return valid, copy_state
    
    def replace_state(self, copy_state):
        print("name the state which you want to remove \n")
        old_state = input("name of the old state \n")
        print("now give information of the new state")
        name_of_new_the_state = input("name: ")
        id_of_the_state = input("Id: ")
        type_of_the_state = input("type: ")

        print("------> here is the copy state \n")
        print(copy_state)

        copy_state[name_of_new_the_state] = copy_state[old_state]
        del copy_state[old_state]

        copy_state[name_of_new_the_state]["id"] = id_of_the_state
        copy_state[name_of_new_the_state]["type"] = type_of_the_state

        # removing all the incoming and outgoing transition to and from the deleted state
        for key in copy_state:
            transitions = copy_state[key].get("transitions", [])
            for transition in transitions:
                if transition.get("target") == old_state:
                    transition["target"] = name_of_new_the_state
                if transition.get("source") == old_state:
                    transition["source"] = name_of_new_the_state        


        print("########> here is the copy state \n")
        print(copy_state)

        # validation check 
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        valid = validate.validation_check(validation_bfs, self.current_state_name, node_lis, "")

        return valid, copy_state 


    def remove_transition(self, copy_state):
        print("From which state the transition occured ?\n")
        name_of_state = input("name: \n")
        name_of_event = input("event: \n")

        copy_state[name_of_state]["transitions"] = [transition for transition in copy_state[name_of_state].get("transitions", []) if transition['event'] != name_of_event]

        # validation check 
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        valid = validate.validation_check(validation_bfs, self.current_state_name, node_lis, "")

        return valid, copy_state 

    def add_transition(self, copy_state):
        print("From which state the transition occured ?\n")
        name_of_the_state = input("name: \n")
        print("which state the transition will go ?\n")
        name_of_the_outgoing_state = input("name\n")
        print("name of the event \n")
        event_name = input("event name \n")

        temp_tran_dic = {"event": event_name, "Source": "", "target": name_of_the_outgoing_state}
        copy_state[name_of_the_state]["transitions"].append(temp_tran_dic)

        # validation check
        validate = Validation(copy_state)
        validation_bfs, reverse_graph, node_lis = validate.graph_build()
        valid = validate.validation_check(validation_bfs, self.current_state_name, node_lis, "")

        return valid, copy_state  



    def replace_transition(self, copy_state):
        pass

    # add, remove and replace state 
    def change_state(self):
        print('1. For adding state \n 2. For removing state \n 3. Replacing state \n 4. Remove transition \n 5. Add Transition \n 6. Replace Transition \n')
        input_option = input("Please select an option ...\n")
        copy_state = copy.deepcopy(self.states) # states
        print(type(copy_state))   
        op = True 
        if input_option == '1':

            # call add state function 
            valid_flag, current_state = self.add_state(copy_state)
            if valid_flag == True:
                # shallow copy 
                self.states = current_state   
                print("Operation is valid\n")
            else:
                print("Invalid operation!\n")
        # remove sate 
        if input_option == '2':
            valid_flag, current_state = self.remove_state(copy_state)
            if valid_flag: 
                # shallow copy 
                self.states = current_state   
                print("Operation is valid\n")
            else:
                print("Invalid Operation!\n")

        # replace state 
        if input_option == '3':
            valid_flag, current_state = self.replace_state(copy_state)

            if valid_flag: 
                # shallow copy 
                self.states = current_state   
                print("Operation is valid\n")
            else:
                print("Invalid Operation!\n")

        # remove transition 
        if input_option == '4':
            valid_flag, current_state = self.remove_transition(copy_state)


            if valid_flag: 
                # shallow copy 
                self.states = current_state   
                print("No warning!! valid\n")
            else:
                print("Warning!\n")
                with open('state_machine/warning.txt', 'r') as file:
                    contents = file.read()
                    print(contents)
                self.states = current_state  

        
        # add transition 
        if input_option == '5':
            valid_flag, current_state = self.add_transition(copy_state)

            if valid_flag == True:
                print("No wanrning !! Valid")
                self.states = current_state  
            else:
                print("Warning!\n")
                with open('state_machine/warning.txt', 'r') as file:
                    contents = file.read()
                    print(contents)
                self.states = current_state

        if input_option == '6':
            print("transition replace is mainly removing and adding a transition \n")
            pass



            



def main():
    # Your main code here
    filename = 'simple_statechart2.json'
    # filename = 'state_chart.json'
    with open(filename, 'r') as file:
    # Deserialize the file content to a Python object
        data = json.load(file)
    while(1):
        var = input('0 to exit\n')
        if var == 0:
            exit
        st_obj = StateMachine(data)
        st_obj.change_state()
        if var == '7':
            st_obj.draw_plant_UML()
    


if __name__ == "__main__":
    main()











        


        #LNg7+-$W9n




