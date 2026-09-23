# restoration_graph.py — problem definition only.
# planner.py must not know anything specific to this file.

ACTIONS = {
    "just_look_at_it": {"requires": set(), "cost": 1},
    "use_telekinesis_to_repair": {"requires": {"just_look_at_it", "focus"}, "cost": 5},
    "focus": {"requires": set(), "cost": 3},
    "scotch_tape": {"requires": {"focus"}, "cost": 1},
    "flex_tape": {"requires": {"just_look_at_it"}, "cost": 3},
}

GOAL = frozenset(ACTIONS.keys())
START = frozenset()

def available_actions(state):
    """Actions whose prerequisites are satisfied and not already done."""
    return [a for a, info in ACTIONS.items()
            if a not in state and info["requires"].issubset(state)]

def apply_action(state, action):
    return state | {action}