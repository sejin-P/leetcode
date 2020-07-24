from typing import List, Text
import logging
#구현할것: leastloadedagent -  load가 least인 agent 이름 반환 skill matching 불필요
#leastflexibleagent - ticket이 허용하는 범위 안에서 skills가 최소인 사람
#조건: load 최대값 3

class NoAgentFoundException(Exception):
    def __init__(self):
        logging.error('cannot find agent')
        super().__init__('cannot find agent')


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self, id, restrictions):
        self.id = id
        self.restrictions = restrictions


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]: # filter numbers of skills first, then by their load
        
        less_worker = []
        for i in range(len(agents)):
            if agents[i].load < 3:
                less_worker.append(i)
        agents = [agents[i] for i in range(len(agents)) if i in less_worker]
        filtered_agents = sorted(agents, key= lambda agent: (len(agent.skills), agent.load))
        return filtered_agents

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        raise NotImplemented


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        min_num = 3
        min_agent = None
        for agent in agents:
            load = agent.load
            if min_num > load:
                min_num = load
                min_agent = agent
        if not min_agent:
            raise NoAgentFoundException
        return min_agent
        


class LeastFlexibleAgent(FinderPolicy):
    def agent_fulfill_restrictions(self, restrictions, skills):
        if len(skills) < len(restrictions):
            return False
        else:
            for restriction in restrictions:
                if restriction in skills:
                    continue
                return False
            return True

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        restrictions = ticket.restrictions
        for agent in self._filter_loaded_agents(agents):
            if not self.agent_fulfill_restrictions(restrictions, agent.skills):
                continue
            else:
                return agent
        raise NoAgentFoundException()

