import csv
import sys

def get_params():
    graph_file = ''
    graph_file = str(input("Insert graph file:\n"))
    domain_name = str(input("Insert Domain file name:\n"))
    problem_name = str(input("Insert Problem file name:\n"))
    gt_o = input("Insert GT Init:\n")
    gl_o = input("Insert GL Init:\n")
    cc_o = input("Insert CC Init:\n")
    gt_d = input("Insert GT Goal:\n")
    gl_d = input("Insert GL Goal:\n")
    cc_d = input("Insert CC Goal:\n")

    print "Init state: " + str(gt_o) + ", " + str(gl_o) + ", " + str(cc_o)
    print "Goal state: " + str(gt_d) + ", " + str(gl_d) + ", " + str(cc_d)
    return graph_file, domain_name, problem_name, gt_o, gl_o, cc_o, gt_d, gl_d, cc_d

#Reads graph file, creates matrix and changes nomenclature for PDDL
def read_graph(graph_reader):

    manip_prim = []

    for row in graph_reader:
        for i in range(0, len(row)-1, 3): #GT
            if row[i].find('2') != -1:
                row[i] = row[i].replace('2','') 
                row[i] = row[i][:2] + '2' + row[i][2:]
        for i in range(len(row)): #Entire data
            if row[i].find('+') != -1:
                row[i] = row[i].replace('+','-') 
                
        manip_prim.append(row)

#    for row in manip_prim:
#        print row

    return manip_prim

def get_predicates(graph_reader):

    gt_all = []
    gl_all = []
    cc_all = []
    actions = []

    n_name=1

    #Get list of Grasp Types
    for row in graph_reader:
        
        #Search Grasp types (in initial states (0) and final states (3))
        for i in range(0, len(row)-1, 3):
            exists = row[i] in gt_all
            if not exists:
                gt_all.append(row[i])

        #Search Grasp locations (in initial states (1) and final states (4))
        for i in range(1, len(row)-1, 3):
            exists = row[i] in gl_all
            if not exists:
                gl_all.append(row[i])

        #Search Cloth Configurations (in initial states (2) and final states (5))
        for i in range(2, len(row)-1, 3):
            exists = row[i] in cc_all
            if not exists:
                cc_all.append(row[i])

        #Search Actions
        exists = row[6] in actions
        if not exists:
            actions.append(row[6])
        else:
            actions.append(row[6]+str(n_name))
            n_name += 1
        #actions.append(row[6])

    print "The Grasping Types (GT) are: " + str(gt_all)
    print "The Grasping Locations (GL) are: " + str(gl_all)
    print "The Cloth Configurations (CC) are: " + str(cc_all)
    print "The Actions are: " + str(actions)

    #Get dimensions to define predicates
    gt_size = len(gt_all)
    gl_size = len(gl_all)
    cc_size = len(cc_all) 
    actions_size = len(actions)

    return gt_all, gl_all, cc_all, actions

def generate_predicates(predicates):
    content = ""
    for preds in predicates:
        content += "(" + preds + ") "
    return content

def generate_actions(manip_prim, all_preds, action_name):
    global actions_content
        
    actions_content += "\t(:action " + action_name + "\n"
    actions_content += "\t\t:precondition (and (" + manip_prim[0] + ") (" + manip_prim[1] + ") (" + manip_prim[2] + "))\n"
    preconds = []
    preconds.append(manip_prim[0])
    preconds.append(manip_prim[1])
    preconds.append(manip_prim[2])
    actions_content += "\t\t:effect (and "

    print "ACTION: " + manip_prim[6]
    print "PRECONDS: " + str(preconds)
    for i in range (0,3):
        print "MANIP: " + manip_prim[i+3]
        exists = manip_prim[i+3] in preconds
        if not exists:
            actions_content += "(" + manip_prim[i+3] + ")"
            actions_content += " (not (" + manip_prim[i] +")) "
#        else:
#            actions_content += " (" + manip_prim[i+3] + ")"

#            adds.append(manip_prim[i+3])
#            dels.append(manip_prim[i])
#    test += "\t\t:effect (and (" + manip_prim[3] + ") (" + manip_prim[4] + ") (" + manip_prim[5] + ") "
    #Write PDDL action
#    actions_content += "\t(:action " + action_name + "\n"
#    actions_content += "\t\t:precondition (and (" + manip_prim[0] + ") (" + manip_prim[1] + ") (" + manip_prim[2] + "))\n"
#    actions_content += "\t\t:effect (and (" + manip_prim[3] + ") (" + manip_prim[4] + ") (" + manip_prim[5] + ") "
#    actions_content += not_pred_content
    actions_content += "))\n"
    actions_content += "\n"
    return actions_content

def generate_actions2(manip_prim, all_preds, action_name):
    global actions_content

    
    not_preds.remove(manip_prim[3])
    not_preds.remove(manip_prim[4])
    not_preds.remove(manip_prim[5])
    not_pred_content = ""
    for not_pred in not_preds:
        not_pred_content += "(not (" + not_pred + ")) "

    #Write PDDL action
    actions_content += "\t(:action " + action_name + "\n"
    actions_content += "\t\t:precondition (and (" + manip_prim[0] + ") (" + manip_prim[1] + ") (" + manip_prim[2] + "))\n"
    actions_content += "\t\t:effect (and (" + manip_prim[3] + ") (" + manip_prim[4] + ") (" + manip_prim[5] + ") "
    actions_content += not_pred_content
    actions_content += "))\n"
    actions_content += "\n"
    return actions_content

def generate_domain(domain_name, gt_all, gl_all, cc_all, actions):
    content = ""
    content += "(define (domain " + str(domain_name) + ")\n"
    content += "\t(:requirements :strips)\n"
    content += "\t(:predicates "
    content += generate_predicates(gt_all) + "\n"
    content += "\t\t\t"
    content += generate_predicates(gl_all) + "\n"
    content += "\t\t\t"
    content += generate_predicates(cc_all) + ")\n"
    content += "\n"
    content += actions
    content += ")"
    return content

def generate_problem(problem_name, domain_name, gt_o, gl_o, cc_o, gt_d, gl_d, cc_d):
    content = ""
    content += "(define (problem " + str(problem_name) + ")\n"
    content += "\t(:domain " + str(domain_name) + ")\n"
    content += "\n"
    content += "(:init (" + str(gt_o) + ") (" + str(gl_o) + ") (" + str(cc_o) + "))\n"
    content += "(:goal (and (" + str(gt_d) + ") (" + str(gl_d) + ") (" + str(cc_d) + ")))\n"
    content += "\n"
    content += ")"

    return content

def main():

#Variables
    gt_all = []
    gl_all = []
    cc_all = []
    actions = []

    graph_file = 'Folding_CloM_Graph.csv'
    domain_name = 'FOLDING'
    problem_name = 'FOLDING'
    gt_o = gt_d = 'Pie'
    gl_o = gl_d = 'I'
    cc_o = 'Crumpled'
    cc_d = 'Folded'
#From graph
#    graph_file, domain_name, problem_name, gt_o, gl_o, cc_o, gt_d, gl_d, cc_d = get_params()
    graph_reader = csv.reader(open(graph_file), delimiter=',') #Open file
    manip_primitives = read_graph(graph_reader)
    gt_all, gl_all, cc_all, actions = get_predicates(manip_primitives)

## Create PDDL domain file
    domain_path = "./domain_" + str(domain_name) + ".pddl"
    domain_file = open(domain_path, "w")
    problem_path = "./problem_" + str(problem_name) + ".pddl"
    problem_file = open(problem_path, "w")

#Create actions
    all_preds = gt_all + gl_all + cc_all
    a = 0
    for row in manip_primitives:
        actions_content = generate_actions(row, all_preds, actions[a])
        a += 1

# Write domain
#    gt_o = 'pie'
#    gl_o = 'null'
#    cc_o = cc_d = 'cr'
#    gt_d = 'pp-pie'
#    gl_d = 'rc'
   
    domain_file.write(generate_domain(domain_name, gt_all, gl_all, cc_all, actions_content))
    #my_file.write(actions_content)
    domain_file.close()
    print("Domain created!")

# Write problem
    problem_file.write(generate_problem(problem_name, domain_name, gt_o, gl_o, cc_o, gt_d, gl_d, cc_d))
    problem_file.close()
    print("Problem created!")


actions_content = ""
main()
