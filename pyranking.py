def rank(
    items: list,
    score_fn: callable,
    reverse: bool = False,
    start: int = 1,
    strategy: str = "competition",
):
    """
    Assign ranking to every item of a list

    :param items: list of items to be ranked
    :param score_fn: function to extract the score from an item
    :param reverse: ranking in ascending order if True, descending order otherwise
    :param start: the first rank number. Default to 1
    :param strategy: to use for ranking. Valid values are:
        competition: Standard competition ranking ("1224" ranking)
        modified-competition: Modified competition ranking ("1334" ranking)
        dense: Dense ranking ("1223" ranking)
        ordinal: Ordinal ranking ("1234" ranking)
        fractional: Fractional ranking ("1 2.5 2.5 4" ranking)
    :return: list of items with their ranking
    """
    ranking_fn = get_ranking_fn(strategy)

    buckets = {}
    for item in items:
        score = score_fn(item)
        buckets[score] = buckets.get(score, []) + [item]

    # sort based on the score
    buckets = sorted(buckets.items(), reverse=(not reverse))

    # assign ranks
    ranked = []
    rank = {"next": start}
    for b in buckets:
        bucket = b[1]
        rank = ranking_fn(rank["next"], len(bucket))
        for i, item in enumerate(bucket):
            ranked.append({"rank": rank["current"][i], "item": item})

    return ranked


def get_ranking_fn(strategy):
    if strategy == "competition":
        return competition_ranking
    elif strategy == "modified-competition":
        return modified_competition_ranking
    elif strategy == "dense":
        return dense_ranking
    elif strategy == "ordinal":
        return ordinal_ranking
    elif strategy == "fractional":
        return fractional_ranking
    else:
        raise ValueError("Invalid ranking strategy")


def competition_ranking(next_rank, num_items):
    current_ranks = [next_rank] * num_items
    next_rank += num_items
    return {"next": next_rank, "current": current_ranks}


def modified_competition_ranking(next_rank, num_items):
    current_ranks = [next_rank + (num_items - 1)] * num_items
    next_rank += num_items
    return {"next": next_rank, "current": current_ranks}


def dense_ranking(next_rank, num_items):
    current_ranks = [next_rank] * num_items
    next_rank += 1
    return {"next": next_rank, "current": current_ranks}


def ordinal_ranking(next_rank, num_items):
    current_ranks = list(range(next_rank, next_rank + num_items))
    next_rank += num_items
    return {"next": next_rank, "current": current_ranks}


def fractional_ranking(next_rank, num_items):
    current_ranks = [next_rank + ((num_items - 1) / 2)] * num_items
    next_rank += num_items
    return {"next": next_rank, "current": current_ranks}
