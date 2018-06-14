import logging

import matplotlib.pyplot as plt

'''plot the value of cost function through generation'''


def annealPlot(anneal):
    if anneal.save:
        plt.plot([i for i in range(len(anneal.costList))], anneal.costList)

        line_init = plt.axhline(y=anneal.initialCost, color="r", linestyle="--")
        line_min = plt.axhline(y=anneal.minCost, color='g', linestyle='--')
        line_right = plt.axhline(y=anneal.problem.standardCost, color="purple", linestyle="--")
        plt.legend([line_init, line_min, line_right], ['Initial weight', 'Optimized weight', 'standard_weight'])
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.annotate("%s" % anneal.minCost, xy=(0, anneal.minCost))
        plt.show()
    else:
        logging.warning("Best solution is : %s, cost function values: %s." % (anneal.bestSolution, anneal.minCost))
        logging.warning("History data not saved. No image to display.")

#
# '''plot details'''
#

# def detailPlot(anneal, generation):
#     list = anneal.acceptHistory[generation]
#     coords = anneal.problem.coords
#
#     xs = []
#     ys = []
#     xs1 = []
#     ys1 = []
#
#     before = list[4]
#     after = list[5]
#     for i in before:
#         xs.append(int(coords[i][0]))
#         ys.append(int(coords[i][1]))
#     for j in after:
#         xs1.append(int(coords[j][0]))
#         ys1.append(int(coords[j][1]))
#     print("---------- generation %d -----------\n" % generation)
#     print("after disturb gets a " + str(list[0]) + ".")
#     flag = ("<" if list[1] < list[2] else ">")
#     print("generated random = %s " % str(list[1]) + flag + " accepance = %s" % str(list[2]))
#     print("the new solution was " + str(list[3]) + ".")
#     print(str(before))
#     print(str(after))
#     print("----------------------------------------")
#
#     plt.title("cost before disturb:%d" % list[6])
#     plt.plot(xs, ys, color="g")
#     plt.show()
#     plt.title("cost after disturb: %d" % list[7])
#     plt.plot(xs1, ys1, color="pink")
#     plt.show()
