import random


def MatchSlugGenerator(match_name, team_one, team_two, match_date):
    slug = random.choice(match_name) + random.choice(match_name) + random.choice(team_one) + random.choice(team_two) + random.choice(team_two) + random.choice(team_two) + random.choice(str(match_date)) + random.choice(str(match_date))
    return slug


def ContestSlugGenerator(contest_name, contest_category, contest_price, contest_fee):
    slug = random.choice(contest_name) + random.choice(contest_name) + random.choice(contest_category) + random.choice(contest_category) + random.choice(str(contest_price)) + random.choice(str(contest_price)) + random.choice(str(contest_fee)) + random.choice(str(contest_fee))
    return slug
