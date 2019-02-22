LEGO City Undercover Map
========================

You can use this map for finding all secrets in Lego City Undercover, different types can be filtered using the legend and you can mark secrets as completed to hide them.

I've used several online guides to complete the map and made corrections, feel free to use my changes. It's also enspired on the "breath-of-the-wild-interactive-map".

The map isn't complete and I can use your help! Please report an issue if you'd like to have something changed or, even better, change it yourself and create a pull request!

All markers are defined in markers.json. To find the coordinates you can add ?debug=1 to the url and click on the map, a popup will appear with the coordinates. With debug enabled the popup for a marker will contain the coordinates.

This map is created using the open source LeafletJS library (many thanks!), I've created the tiles by screenshotting the map on a Nintendo Switch and shared the pictures on Facebook, removed the HUD using Imagemagick and glued them back together using GIMP. This way I've created a baselayer which I've aligned to the top left and cropped at 4096x4096 pixels. This image was cropped and scaled to tiles using crop_legocity.png.

The map can be visited at:
https://meeuw.github.io/legocityundercovermap/

The completion data is stored as localeStorage in your browser, as the markers are still being updated the completion data might get garbled. Please make sure you've forked the map to make sure your completion data will not be corrupted.
