* Glossary
  * __room__: A single rectangular area within a stage. The camera is constrained to stay within the bounds of the current room at all times. Rooms may be connected through explicit doors, or at their edges.
  * __door__: A fixture or frob that, when interacted with, changes the user's location, possibly to a different room.
  * __frob__: "Free object". An object that can move within a room, unconstrained to the grid. All player sprites are frobs, as are interactable blocks and NPCs and so on. Particles are also not frobs, but fall under the category of effects.
  * __sprite__: The graphic representation of a user. Can have multiple pieces arranged using a template (e.g. humanoid).
  * __fixture__: A tile that can be interacted with. Doors can be fixtures. These are simpler to deal with than frobs because physics doesn't need to apply to them; they always stay in one place.
  * __effect__: A cosmetic effect (like a particle system). Can be emitted by a script, but never synced.
  * __script__: Code run by a fixture, frob, or room. Can have multiple states, each containing a set of actions and a set of conditions (to possibly change state).
  * __animation__: A sequence of frames and timings. Can be composed of multiple frames at once in the case of a multi-part sprite.
  * __frame__: A static image of a fixture, frob, or sprite piece. Used in animation. Can define connection points.
  * __connection point__: The place where two sprite pieces are constrained to intersect (e.g. chest to shoulder)
  
* Client
  * Rooms
    * Read from server
      * Define JSON-based format
    * Place frobs in room
    * Run scripts
  * Graphics
    * Render room tiles
    * Render simple sprites
    * Render 
  * Sound
  * Input
    * Generalized 'controller'
  * Physics
    * Note: don't go crazy with this! We are going for 'good enough', not perfect realism
    * Gravity
    * Collision detection (this needs to work well)
    * Friction
    * Moving platforms
  * Network
    * Synchronize room state with server
    * Send messages to other users
* Server