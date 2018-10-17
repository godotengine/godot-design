# Design elements for Godot

## Purposes of this repository

- Share ideas, proposals and assets related to Godot's user experience.
- Discuss the proposed ideas in order to make them better and reach consensus.
- Provide high-quality assets and UX recommendations for Godot.

## Repository structure

- **`archives`:** Anything deprecated should go to this folder.
- **`communication`:** Everything needed for communication such as flyers,
  posters, banners, …
- **`concepts`:** Here to store design ideas, fan art, …
- **`engine`:** Everything included into the Godot editor (especially icons).
- **`godette`:** Designs for the personified Godot character.
- **`goodies`:** T-shirts, mugs, stickers, business cards, …
- **`screenshots`:** Screenshots of the editor to use for demonstration
  purposes.
- **`wallpapers`**: Official or fan-made wallpapers.
- **`websites`:** Everything related to Godot's Web presence or communities.

## Icon optimization

Editor icons must be first optimized before being added to the engine, to do so:
- Add them to the "/engine/icons/svg" folder.
- Run the "optimize.py" script (you must have `scour` installed).

The optimized icons will be generated in the "/engine/icons/optimized" folder.

## License

Unless otherwise specified, files contained in this repository are licensed
under CC BY 4.0 International, as described in the [`LICENSE`](/LICENSE) file.
