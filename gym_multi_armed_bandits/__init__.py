from gym.envs.registration import register

register(
    id='multi-armed-bandits-v0',
    entry_point='gym_multi_armed_bandits.envs:MultiArmedBanditsEnv',
)
