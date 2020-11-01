from collections import OrderedDict
import numpy as np

# from robosuite.utils.transform_utils import convert_quat
from robosuite.environments.sawyer import SawyerEnv

# from robosuite.models.arenas import TableArena
from robosuite.models.arenas import EmptyArena
# from robosuite.models.robots import Sawyer
# from robosuite.models.objects import BoxObject

# from robosuite.models.tasks import TableTopTask
from robosuite.models import MujocoWorldBase

class SawyerViz(SawyerEnv):
    """
    Sawyer robot arm visualization.
    """

    def __init__(
        self,
        gripper_type="TwoFingerGripper",
        use_camera_obs=True,
        use_object_obs=True,
        reward_shaping=False,
        gripper_visualization=False,
        has_renderer=False,
        has_offscreen_renderer=True,
        render_collision_mesh=False,
        render_visual_mesh=True,
        control_freq=10,
        horizon=1000,
        ignore_done=False,
        camera_name="frontview",
        camera_height=256,
        camera_width=256,
        camera_depth=False,
    ):
        """
        Args:

            gripper_type (str): type of gripper, used to instantiate
                gripper models from gripper factory.

            use_camera_obs (bool): if True, every observation includes a
                rendered image.

            use_object_obs (bool): if True, include object (cube) information in
                the observation.

            reward_shaping (bool): if True, use dense rewards.

            gripper_visualization (bool): True if using gripper visualization.
                Useful for teleoperation.

            has_renderer (bool): If true, render the simulation state in
                a viewer instead of headless mode.

            has_offscreen_renderer (bool): True if using off-screen rendering.

            render_collision_mesh (bool): True if rendering collision meshes
                in camera. False otherwise.

            render_visual_mesh (bool): True if rendering visual meshes
                in camera. False otherwise.

            control_freq (float): how many control signals to receive
                in every second. This sets the amount of simulation time
                that passes between every action input.

            horizon (int): Every episode lasts for exactly @horizon timesteps.

            ignore_done (bool): True if never terminating the environment (ignore @horizon).

            camera_name (str): name of camera to be rendered. Must be
                set if @use_camera_obs is True.

            camera_height (int): height of camera frame.

            camera_width (int): width of camera frame.

            camera_depth (bool): True if rendering RGB-D, and RGB otherwise.
        """

        # settings for table top
        # TODO (chongyi zheng)
        # self.table_full_size = table_full_size
        # self.table_friction = table_friction

        # whether to use ground-truth object states
        # self.use_object_obs = use_object_obs

        # reward configuration
        self.reward_shaping = reward_shaping

        # TODO (chongyi zheng)
        # object placement initializer
        # if placement_initializer:
        #     self.placement_initializer = placement_initializer
        # else:
        #     # (chongyi zheng): move the pesky colorful object outside the camera field of view.
        #     self.placement_initializer = UniformRandomSampler(
        #         x_range=[-0.03, 0.03],
        #         y_range=[-0.03, 0.03],
        #         ensure_object_boundary_in_range=False,
        #         z_rotation=True,
        #     )

        super().__init__(
            gripper_type=gripper_type,
            gripper_visualization=gripper_visualization,
            use_indicator_object=False,
            has_renderer=has_renderer,
            has_offscreen_renderer=has_offscreen_renderer,
            render_collision_mesh=render_collision_mesh,
            render_visual_mesh=render_visual_mesh,
            control_freq=control_freq,
            horizon=horizon,
            ignore_done=ignore_done,
            use_camera_obs=use_camera_obs,
            camera_name=camera_name,
            camera_height=camera_height,
            camera_width=camera_width,
            camera_depth=camera_depth,
        )

    def _load_model(self):
        """
        Loads an xml model, puts it in self.model
        """
        super()._load_model()
        self.mujoco_robot.set_base_xpos([0, 0, 0])

        # load model for table top workspace
        self.mujoco_arena = EmptyArena()
        # if self.use_indicator_object:
        #     self.mujoco_arena.add_pos_indicator()

        # The sawyer robot has a pedestal, we want to align it with the table
        # TODO (chongyi zheng)
        # self.mujoco_arena.set_origin([0.16 + self.table_full_size[0] / 2, 0, 0])

        # initialize objects of interest
        # TODO (chongyi zheng)
        # cube = BoxObject(
        #     size_min=[0.020, 0.020, 0.020],  # [0.015, 0.015, 0.015],
        #     size_max=[0.022, 0.022, 0.022],  # [0.018, 0.018, 0.018])
        #     rgba=[1, 0, 0, 1],
        # )
        # self.mujoco_objects = OrderedDict([("cube", cube)])
        # self.mujoco_objects = OrderedDict([])

        # TODO (chongyi zheng)
        self.model = MujocoWorldBase()
        self.model.merge(self.mujoco_arena)
        self.model.merge(self.mujoco_robot)
        # task includes arena, robot, and objects of interest
        # self.model = TableTopTask(
        #     self.mujoco_arena,
        #     self.mujoco_robot,
        #     self.mujoco_objects,
        # )
        # self.model.place_objects()

    def _get_reference(self):
        """
        Sets up references to important components. A reference is typically an
        index or a list of indices that point to the corresponding elements
        in a flatten array, which is how MuJoCo stores physical simulation data.
        """
        # TODO (chongyi zheng)
        super()._get_reference()
        # self.cube_body_id = self.sim.model.body_name2id("cube")
        # self.l_finger_geom_ids = [
        #     self.sim.model.geom_name2id(x) for x in self.gripper.left_finger_geoms
        # ]
        # self.r_finger_geom_ids = [
        #     self.sim.model.geom_name2id(x) for x in self.gripper.right_finger_geoms
        # ]
        # self.cube_geom_id = self.sim.model.geom_name2id("cube")

    def _reset_internal(self):
        """
        Resets simulation internal configurations.
        """
        super()._reset_internal()

        # TODO (chongyi zheng)
        # reset positions of objects
        # self.model.place_objects()

        # reset joint positions
        # init_pos = np.array([-0.5538, -0.8208, 0.4155, 1.8409, -0.4955, 0.6482, 1.9628])
        # init_pos += np.random.randn(init_pos.shape[0]) * 0.02
        # self.sim.data.qpos[self._ref_joint_pos_indexes] = np.array(init_pos)

    def reward(self, action=None):
        """
        Reward function for the task.

        The dense reward has three components.

            Reaching: in [0, 1], to encourage the arm to reach the cube
            Grasping: in {0, 0.25}, non-zero if arm is grasping the cube
            Lifting: in {0, 1}, non-zero if arm has lifted the cube

        The sparse reward only consists of the lifting component.

        Args:
            action (np array): unused for this task

        Returns:
            reward (float): the reward
        """
        reward = 0.

        # TODO (chongyi zheng)
        # # sparse completion reward
        # if self._check_success():
        #     reward = 1.0
        #
        # # use a shaping reward
        # if self.reward_shaping:
        #
        #     # reaching reward
        #     cube_pos = self.sim.data.body_xpos[self.cube_body_id]
        #     gripper_site_pos = self.sim.data.site_xpos[self.eef_site_id]
        #     dist = np.linalg.norm(gripper_site_pos - cube_pos)
        #     reaching_reward = 1 - np.tanh(10.0 * dist)
        #     reward += reaching_reward
        #
        #     # grasping reward
        #     touch_left_finger = False
        #     touch_right_finger = False
        #     for i in range(self.sim.data.ncon):
        #         c = self.sim.data.contact[i]
        #         if c.geom1 in self.l_finger_geom_ids and c.geom2 == self.cube_geom_id:
        #             touch_left_finger = True
        #         if c.geom1 == self.cube_geom_id and c.geom2 in self.l_finger_geom_ids:
        #             touch_left_finger = True
        #         if c.geom1 in self.r_finger_geom_ids and c.geom2 == self.cube_geom_id:
        #             touch_right_finger = True
        #         if c.geom1 == self.cube_geom_id and c.geom2 in self.r_finger_geom_ids:
        #             touch_right_finger = True
        #     if touch_left_finger and touch_right_finger:
        #         reward += 0.25

        return reward

    def _get_observation(self):
        """
        Returns an OrderedDict containing observations [(name_string, np.array), ...].

        Important keys:
            robot-state: contains robot-centric information.
            object-state: requires @self.use_object_obs to be True.
                contains object-centric information.
            image: requires @self.use_camera_obs to be True.
                contains a rendered frame from the simulation.
            depth: requires @self.use_camera_obs and @self.camera_depth to be True.
                contains a rendered depth map from the simulation
        """
        di = super()._get_observation()
        # camera observations
        if self.use_camera_obs:
            camera_obs = self.sim.render(
                camera_name=self.camera_name,
                width=self.camera_width,
                height=self.camera_height,
                depth=self.camera_depth,
            )
            if self.camera_depth:
                di["image"], di["depth"] = camera_obs
            else:
                di["image"] = camera_obs

        # TODO (chongyi zheng)
        # low-level object information
        # if self.use_object_obs:
        #     # position and rotation of object
        #     cube_pos = np.array(self.sim.data.body_xpos[self.cube_body_id])
        #     cube_quat = convert_quat(
        #         np.array(self.sim.data.body_xquat[self.cube_body_id]), to="xyzw"
        #     )
        #     di["cube_pos"] = cube_pos
        #     di["cube_quat"] = cube_quat
        #
        #     gripper_site_pos = np.array(self.sim.data.site_xpos[self.eef_site_id])
        #     di["gripper_to_cube"] = gripper_site_pos - cube_pos
        #
        #     di["object-state"] = np.concatenate(
        #         [cube_pos, cube_quat, di["gripper_to_cube"]]
        #     )

        return di

    def _check_contact(self):
        """
        Returns True if gripper is in contact with an object.
        """
        collision = False
        for contact in self.sim.data.contact[: self.sim.data.ncon]:
            if (
                self.sim.model.geom_id2name(contact.geom1)
                in self.gripper.contact_geoms()
                or self.sim.model.geom_id2name(contact.geom2)
                in self.gripper.contact_geoms()
            ):
                collision = True
                break
        return collision

    def _check_success(self):
        """
        Returns True if task has been completed.
        """
        # TODO (chongyi zheng)
        # cube_height = self.sim.data.body_xpos[self.cube_body_id][2]
        # table_height = self.table_full_size[2]
        #
        # # cube is higher than the table top above a margin
        # return cube_height > table_height + 0.04
        raise NotImplementedError

    def _gripper_visualization(self):
        """
        Do any needed visualization here. Overrides superclass implementations.
        """

        # color the gripper site appropriately based on distance to cube
        if self.gripper_visualization:
            # TODO (chongyi zheng)
            # # get distance to cube
            # cube_site_id = self.sim.model.site_name2id("cube")
            # dist = np.sum(
            #     np.square(
            #         self.sim.data.site_xpos[cube_site_id]
            #         - self.sim.data.get_site_xpos("grip_site")
            #     )
            # )

            # set RGBA for the EEF site here
            # max_dist = 0.1
            # scaled = (1.0 - min(dist / max_dist, 1.)) ** 15
            scaled = 0.0
            rgba = np.zeros(4)
            rgba[0] = 1 - scaled
            rgba[1] = scaled
            rgba[3] = 0.5

            self.sim.model.site_rgba[self.eef_site_id] = rgba
