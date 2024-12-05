from pathlib import Path
from day_05_1 import read_rules_and_updates, Rule, Update, PageOrder, establish_page_order, is_update_in_order, \
    get_middle_page


def order_update(update: Update, page_order: PageOrder) -> Update:
    for i in range(1, len(update)):
        if update[i] not in page_order:
            continue
        if any([lower_page in update[:i] for lower_page in page_order[update[i]]]):
            update = put_page_in_proper_place(update, i, page_order[update[i]])
    return update


def put_page_in_proper_place(update: Update, element_position: int, lower_pages: list[int]) -> Update:
    element = update[element_position]
    update = update[:element_position] + update[element_position + 1:]
    for j in range(len(update)):
        if update[j] in lower_pages:
            return update[:j] + [element] + update[j:]
    raise RuntimeError("Proper place not found")


def main():
    rules, updates = read_rules_and_updates(Path("input.txt"))
    page_order = establish_page_order(rules)
    updates_not_in_order = [update for update in updates if not is_update_in_order(update, page_order)]
    ordered_updates = [order_update(update, page_order) for update in updates_not_in_order]
    print(sum([get_middle_page(update) for update in ordered_updates]))


if __name__ == '__main__':
    main()
