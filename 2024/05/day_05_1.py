from pathlib import Path

Rule = tuple[int, int]
Update = list[int]
PageOrder = dict[int, list[int]]


def read_rules_and_updates(input_path: Path) -> tuple[list[Rule], list[Update]]:
    rules = []
    updates = []
    lines = input_path.read_text().splitlines()
    for line in lines:
        if '|' in line:
            rules.append(parse_rule(line))
        if ',' in line:
            updates.append(parse_update(line))
    return rules, updates


def parse_rule(rule: str) -> Rule:
    rule_split = rule.split('|')
    return int(rule_split[0]), int(rule_split[1])


def parse_update(update: str) -> Update:
    update = update.split(',')
    return list(map(int, update))


def establish_page_order(rules: list[Rule]) -> PageOrder:
    page_order: PageOrder = {}
    for rule in rules:
        page_a, page_b = rule
        page_order.setdefault(page_a, []).append(page_b)
    return page_order


def is_update_in_order(update: Update, page_order: PageOrder) -> bool:
    for i in range(1, len(update)):
        if update[i] not in page_order:
            continue
        if any([lower_page in update[:i] for lower_page in page_order[update[i]]]):
            return False
    return True


def get_middle_page(update: Update) -> int:
    return update[len(update) // 2]


def main():
    rules, updates = read_rules_and_updates(Path("input.txt"))
    page_order = establish_page_order(rules)
    print(sum([get_middle_page(update) for update in updates if is_update_in_order(update, page_order)]))

if __name__ == '__main__':
    main()
