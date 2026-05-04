import utils
import random
import copy
import math


def simulated_annealing(map, T_min, T_initial, cooling_rate):
    """
    Optimize hospital positions using simulated annealing by exploring random moves
    and occasionally accepting worse states to escape local optima.

    Args:
        map: Matrix (list of lists) representing the board.
        T_min: Minimum temperature at which the search stops.
        T_initial: Starting temperature for the annealing process.
        cooling_rate: Multiplicative factor used to cool the temperature each step.

    Returns:
        list[list]: A grid configuration produced by the annealing search.
    """

    current_map = copy.deepcopy(map)
    current_cost = utils.cost(current_map)
    temperature = T_initial

    while temperature > T_min:
        best_map = current_map
        best_cost = current_cost
        hospitals = utils.find_objects(current_map, utils.OBJECT_HOSPITAL)

        if not hospitals:
            continue

        canditate_hospital = random.choice(hospitals)
        moves_list = utils.actions(current_map, canditate_hospital)

        if not moves_list:
            continue

        candidate_move = random.choice(moves_list)
        candidate_map = utils.result(current_map, canditate_hospital, candidate_move)
        candidate_cost = utils.cost(candidate_map)

        cost_difference = candidate_cost - current_cost

        if candidate_cost < best_cost:
            best_map = candidate_map
            best_cost = candidate_cost
        else:
            random_num = random.random()
            acceptance = math.exp(-cost_difference / temperature)
            if random_num < acceptance:
                best_map = candidate_map
                best_cost = candidate_cost

        temperature = temperature * cooling_rate

        current_map = best_map
        current_cost = best_cost

    return current_map
