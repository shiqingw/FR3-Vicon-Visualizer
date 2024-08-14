from FR3ViconVisualizer.fr3_mj_env_collision_flying_ball import FR3MuJocoEnv
import time
if __name__ == '__main__':
    env = FR3MuJocoEnv()
    env.reset()
    for i in range(10):
        time.sleep(1)
    env.close()