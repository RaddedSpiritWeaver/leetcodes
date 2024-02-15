#   this was my first working solution.
#   pretty slow... :)

from typing import List


class Solution:
    def get_valid_actions(
        self, field_shape: tuple, current_loc: tuple, parent: bool
    ) -> list[tuple]:
        result = []
        if not parent:
            next_i = current_loc[0] + 1
        else:
            next_i = current_loc[0] - 1

        #   check i
        if next_i >= field_shape[0] or next_i < 0:
            return result

        for step in range(-1, 2):
            next_j = current_loc[1] + step
            #   check j
            if next_j < 0 or next_j >= field_shape[1]:
                continue
            result.append((next_i, next_j))

        return result

    def get_next_nodes(self, pos_a: tuple, pos_b: tuple, board_shape: tuple):
        a_next = self.get_valid_actions(board_shape, pos_a, parent=False)
        b_next = self.get_valid_actions(board_shape, pos_b, parent=False)
        res = []
        for a in a_next:
            for b in b_next:
                res.append((a, b))
        return res

    def build_up(self, board: list[list[int]]):
        board_shape = (len(board), len(board[0]))
        #   use key format: i::aj__bj
        max_rewards = {}
        fathers = {}

        #   do the first level
        positions = ((0, 0), (0, board_shape[1] - 1))
        position_key = f"{0}::{0}__{board_shape[1] - 1}"
        max_reward_level_0 = board[0][0] + board[0][board_shape[1] - 1]
        max_rewards[position_key] = max_reward_level_0
        #   child expansion
        frontier = self.get_next_nodes(positions[0], positions[1], board_shape)
        for child in frontier:
            child_key = f"{child[0][0]}::{child[0][1]}__{child[1][1]}"
            try:
                fathers[child_key].append(positions)
            except KeyError:
                fathers[child_key] = [positions]

        while frontier:
            positions = frontier.pop(0)
            position_key = f"{positions[0][0]}::{positions[0][1]}__{positions[1][1]}"
            if position_key in max_rewards:
                continue
            # if positions[0] == positions[1]: continue
            mirror_key = f"{positions[0][0]}::{positions[1][1]}__{positions[0][1]}"
            if mirror_key in max_rewards:
                continue
            #   get parents
            parents = fathers[position_key]

            #   select max parent
            max_val = -1
            for parent in parents:
                parent_key = f"{parent[0][0]}::{parent[0][1]}__{parent[1][1]}"
                if max_val < max_rewards[parent_key]:
                    max_val = max_rewards[parent_key]

            #   update the max value for current state
            if positions[0][1] == positions[1][1]:
                #   only one robot takes it
                current_reward = max_val + board[positions[0][0]][positions[0][1]]
            else:
                current_reward = (
                    max_val
                    + board[positions[0][0]][positions[0][1]]
                    + board[positions[0][0]][positions[1][1]]
                )

            max_rewards[position_key] = current_reward

            #   child expansion
            children = self.get_next_nodes(positions[0], positions[1], board_shape)
            for child in children:
                child_key = f"{child[0][0]}::{child[0][1]}__{child[1][1]}"
                try:
                    fathers[child_key].append(positions)
                except KeyError:
                    fathers[child_key] = [positions]

            frontier = frontier + [x for x in children if x not in max_rewards]

        return max_rewards

    def cherryPickup(self, grid: List[List[int]]) -> int:
        #   just to pass an empty grid
        x = 0
        x = sum([sum(i) for i in grid])
        if x == 0:
            return 0
        
        max_rewards = self.build_up(grid)

        max = -1
        i = len(grid) - 1
        max_j = len(grid[0])
        for j in range(max_j):
            for k in range(max_j):
                key = f"{i}::{j}__{k}"
                try:
                    if max < max_rewards[key]:
                        max = max_rewards[key]
                except KeyError:
                    pass

        return max
