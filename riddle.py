import random


def main():
    people_in_game = 100
    total_game_plays = 10_000

    for strategy in [try_random_strategy, try_looping_strategy]:
        total_fails = play_game(people_in_game, total_game_plays, strategy)
        fail_percentage = (total_fails / total_game_plays) * 100.0
        print(
            f"With {people_in_game} people, got {total_fails:,} fails out of {total_game_plays:,} plays"
            f" ({fail_percentage:.9f}%) using the {strategy.__name__} strategy"
        )


def try_random_strategy(num_people, index, arr):
    tries = list(range(num_people))
    random.shuffle(tries)
    tries = tries[0 : int(num_people / 2)]
    for each_try in tries:
        if each_try == arr[index]:
            return True
    return False


def try_looping_strategy(num_people, index, arr):
    num_tries = int(num_people / 2)
    index_to_try_next = index
    for _ in range(num_tries):
        if arr[index_to_try_next] == index:
            return True
        else:
            index_to_try_next = arr[index_to_try_next]
    return False


def play_game(num_people, num_iterations, strategy_func):
    assert num_people % 2 == 0 and num_people > 0
    arr = list(range(num_people))
    total_failures = 0
    for iteration in range(num_iterations):
        random.shuffle(arr)
        failure = False
        for person_index in range(num_people):
            if failure:
                continue
            if not strategy_func(num_people, person_index, arr):
                failure = True
                total_failures += 1
        if (iteration + 1) % 10_000 == 0:
            print(f"Done with {iteration+1:,} iterations...")

    return total_failures


if __name__ == "__main__":
    main()
