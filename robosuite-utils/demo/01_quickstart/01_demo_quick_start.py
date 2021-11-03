import numpy as np
import robosuite as suite

# create environment instance
# env = suite.make(
#     env_name="TwoArmLift",  # try with other tasks like "Stack" and "Door"
#     robots="Panda",  # try with other robots like "Sawyer" and "Jaco"
#     has_renderer=True,
#     has_offscreen_renderer=False,
#     use_camera_obs=False,
#     # render_camera="robot0_eye_in_hand",
#     hard_reset=False,
#     ignore_done=True
#     # use_object_obs=False,
# )

env = suite.make(
    "Stack",      # environment name (see below)
    "Panda",
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
    # render_camera="robot0_eye_in_hand",
    hard_reset=False,
    ignore_done=True,
    # use_object_obs=False,
)

# reset the environment
print(env.reset())
for j in range(len(env.robots[0].joint_indexes)):
    print("Joint ID:", j, ",", "Joint Name:", env.sim.model.joint_id2name(
        j), ",", "Joint Limits", env.sim.model.jnt_range[j])

for i in range(1000):
    # action = np.random.randn(env.robots[0].dof)  # sample random action
    action = [0, 0, 0, 0, 0, 0, 0, 1]  # sample random action
    # take action in the environment
    obs, reward, done, info = env.step(action)
    env.render()  # render on display

# print(done)
