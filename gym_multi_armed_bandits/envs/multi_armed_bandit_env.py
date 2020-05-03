import gym
from gym import spaces
from gym.utils import seeding


class MultiArmedBanditsEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, nb_bandits=10, seed=None):
        self.seed(seed=seed)
        self.bandits = self.rng.random.normal(
            loc=0.0,
            scale=1.0,
            size=nb_bandits
        )
        self.action_space = spaces.Discrete(nb_bandits)
        self.observation_space = spaces.Discrete(1)

    def step(self, action):
        assert self.action_space.contains(action)
        observation = None  # agent's observation of the current environment
        reward = self.self.rng.random.normal(
            loc=self.bandits[action],
            scale=1.0
        )
        done = True  # whether the episode has ended, in which case further
        # step() calls will return undefined results
        info = {}  # contains auxiliary diagnostic information (helpful for
        # debugging, and sometimes learning)
        return observation, reward, done, info

    def reset(self):
        observation = None
        return observation

    def render(self, mode='human'):
        pass

    def close(self):
        pass

    def seed(self, seed=None):
        self.rng, seed = seeding.np_random(seed=seed)
        return [seed]
