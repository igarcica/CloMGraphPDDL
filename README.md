
# Knowledge Representation for High-level Planning in Cloth Manipulation Tasks

Repository used in the article of the same title submitted to ICAPS workshops on Knowledge Engineering for Planning and Scheduling (KEPS22) to generate domain models in PDDL of a cloth manipulation task.
Institut de Robòtica i Informàtica Industrial, CSIC-UPC. Author Irene Garcia-Camacho (igarcia@iri.upc.edu).


## Execution

To generate the domain and problem files, make sure you have the CloM Graph data (file Folding_CloM_Graph.csv) and run the python script as:

``python ./pddl_generator.py``

The output will provide two LISP-like files named *domain_FOLDING.pddl* and *problem_FOLDING.pddl*

Once having the domain model it can be solved by using a planner solver. In our example we used the Fast-Forward solver [1]. Download the solver and add its path to your env as:

``export PATH=$PATH:~/Metric-FF-v2.1``

To obtain the result of the problem run:

``ff -o domain_FOLDING.pddl -f problem_FOLDING.pddl -s 0``

## Dependencies

-Python3
    - Graphviz ``sudo apt install python3-graphviz``

-Fast-Forward solver [1]

## References

[1] https://fai.cs.uni-saarland.de/hoffmann/metric-ff.html (Download version 2.1)
