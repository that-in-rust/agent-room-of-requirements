# Force Graph And Scene Checklist

Use this when the task includes force graphs, dense node-link views, or camera-driven 3D exploration.

## Interaction

- Is selection stable after data refresh?
- Can the user recover orientation with reset or fit-to-view?
- Are hover and click distinct in code and behavior?
- Does keyboard or panel navigation mirror what the pointer can do?

## Data Volume

- Can labels be culled or simplified?
- Can expensive node geometry degrade at high counts?
- Are derived metrics cached instead of recomputed per frame?

## Rendering

- Are materials and geometries reused where possible?
- Are heavy textures, sprites, or labels lazily enabled?
- Is camera animation bounded so it cannot thrash on repeated events?

## Reliability

- Does the canvas handle disconnects, empty graphs, and partial data?
- Are subscriptions or animation loops torn down on unmount?
- Is there a plain fallback if WebGL is unavailable?
