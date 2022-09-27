from search.models import Academic, News, Org, Research


class Categorizer:
    def __init__(self):
        self.credible = {}
        self.credible["news"] = ["donga", "chosun", "joongang", "hani"]
        self.credible["academic"] = ["ac.kr", "udacity", "udemy"]
        self.credible["org"] = [".org"]
        self.credible["research"] = ["kiss", "dbpia"]
        self.news_count = 0
        self.org_count = 0
        self.academic_count = 0
        self.research_count = 0

    def get_category(self, link):
        for category, keywords in self.credible.items():
            for keyword in keywords:
                if keyword in link:
                    return category
        return "other"

    def save(self, category, element):
        if category == "news" and self.news_count == 0:
            News(
                title=element["title"],
                link=element["link"],
                description=element["snippet"],
            ).save()
            self.news_count += 1
        elif category == "org" and self.org_count == 0:
            Org(
                title=element["title"],
                link=element["link"],
                description=element["snippet"],
            ).save()
            self.org_count += 1
        elif category == "research" and self.research_count == 0:
            Research(
                title=element["title"],
                link=element["link"],
                description=element["snippet"],
            ).save()
            self.research_count += 1
        elif category == "academic" and self.academic_count == 0:
            Academic(
                title=element["title"],
                link=element["link"],
                description=element["snippet"],
            ).save()
            self.academic_count += 1
        else:
            pass
