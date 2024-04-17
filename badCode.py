import random
from Benchmarking.profiling.intrusive import collect_measurements
from Benchmarking import benchmark as mb


# decorate your function to be able to collect measurements.

maxTreeLife = 150
treeCount = 5000

@collect_measurements(test_case_name="bad test", enabled=True)
def main():
    trees = spawnTrees(treeCount)
    printData(trees)
    data = simulation(trees, 10000)
    printData(data)


def spawnTrees(count):
    #TODO: spawn trees
    tree = []
    for t in range(count):
        #tree.append({"age": random.randint(0, maxTreeLife), "size": random.randint(0, 3)})
        tree.append(random.randint(0, maxTreeLife))
    return(tree)

def simulationStep(data):
    addTree = 0
    removeTree =[]
    for t in range(len(data)):
        data[t] += 1
        if data[t] > 20: 
            if random.randint(0, 100) == 10:
                addTree += 1
        if data[t] > maxTreeLife:
            if random.randint(0, 20) == 10:        
                removeTree.append(t)
    for a in range(0, addTree): 
        data.append(random.randint(0, maxTreeLife))
    removeTree.sort(reverse=True)
    for r in range(0, len(removeTree)):
            del data[removeTree[r]]

    return data

def simulation(data, length):
    for s in range(length):
        data = simulationStep(data)
    return data
    #TODO: do the simulation


def printData(data):
    print ("there are: ", len(data), " trees")
    print("data:")
    #print(data)
    #TODO: print things out


# Give your benchmark a name
mb.test_case_name = "bad test"

# Define you benchmark
mb.run(
    method=main,  # <-- Make sure you don't call the method
    arguments=[],
    iteration=100,
    pacing=0,
    processes=2
)

# Get a letter rank how your changes compare to a previous benchmark.
letter_rank = mb.regression.letter_rank  # > A+

print(mb.test_id)
print(mb.test_case_name)
print(mb.regression.letter_rank)