# this is a very quick-n-dirty script to optimize SVGS and generate
# darker variations for white themes.
#

from os import listdir, mkdir
from os.path import isfile, join, dirname, realpath, isdir
import subprocess
import re

import hashlib

out_path = 'optimized_gen'
svgs_path = 'svg'

file_names = [f for f in listdir(svgs_path) if isfile(join(svgs_path, f))]



colors = {
	"#e0e0e0": "#4f4f4f", # common icon color
	"#ffffff": "#000000", # white
	"#b4b4b4": "#000000", # script darker color

	"#cea4f1": "#bb6dff", # animation
	"#fc9c9c": "#ff5f5f", # spatial
	"#a5b7f3": "#6d90ff", # 2d
	"#708cea": "#0843ff", # 2d dark
	"#a5efac": "#29d739", # control

	"#ff8484": "#ff3333", # error
	"#84ffb1": "#00db50", # success
	"#ffd684": "#ffad07", # warning

	# rainbow
	"#ff7070": "#ff2929", # red
	"#ffeb70": "#ffe337", # yellow
	"#9dff70": "#74ff34", # green
	"#70ffb9": "#2cff98", # aqua
	"#70deff": "#22ccff", # blue
	"#9f70ff": "#702aff", # purple
	"#ff70ac": "#ff2781", # pink

	# audio gradient
	"#ff8484": "#ff4040", # red
	"#e1dc7a": "#d6cf4b", # yellow
	"#84ffb1": "#00f010", # green

	"#ffd684": "#fea900", # mesh (orange)
	"#40a2ff": "#68b6ff", # shape (blue)

	"#84c2ff": "#5caeff", # selection (blue)

	"#ea686c": "#e3383d", # key xform (red)
}

exceptions = ["icon_editor_pivot", "icon_editor_handle", "icon_editor_3d_handle", 
	"icon_godot", "icon_panorama_sky", "icon_procedural_sky", "icon_editor_control_anchor",
	"icon_default_project_icon"
]


hashes = {}


generate_darks = False


try:
	with open("hashes", "r") as f:
		for l in f.readlines():
			n, h = l.strip().split(" ")
			hashes[n] = h

except:
	open("hashes", "w")


if not isdir("%s" % out_path):
	mkdir("%s" % out_path)
if generate_darks:
	if not isdir("%s/dark" % out_path):
		mkdir("%s/dark" % out_path)



scour_options = " ".join([
	"--enable-id-stripping",
	"--enable-comment-stripping",
	"--shorten-ids",
	"--indent=none",
	"--strip-xml-prolog",
	"--remove-descriptive-elements",
	"--enable-comment-stripping"
])


current = 0
for file_name in file_names:
	current += 1
	name_only = file_name.replace('.svg', '')

	with open('{}/{}.svg'.format(svgs_path, name_only), 'r') as svgo:
		svg_str = svgo.read();
		m = hashlib.md5(svg_str.encode()).hexdigest()
		if hashes.get(name_only) == m:
			continue
		else:
			hashes[name_only] = m

	print("%s - %s of %s" % (file_name, current, len(file_names)))

	subprocess.call(
		"scour -q -i {svgs_dir}/{file_name}.svg -o {output_dir}/{file_name}.svg {options}"
		.format(file_name=name_only, output_dir=out_path, svgs_dir=svgs_path, options=scour_options), 
		shell=True
	)

	if generate_darks:
		color_re = r"(#[0-9A-Fa-f]{6})|(#[0-9A-Fa-f]{3})"

		with open('{}/{}.svg'.format(out_path, name_only), 'r') as svg:
			svg_str = svg.read();

			if not name_only in exceptions:
				for m in re.finditer(color_re, svg_str):
					color = m.group(0)
					if len(color) == 4:
						color = "#{}{}{}".format(color[1] * 2, color[2] * 2, color[3] * 2)
					new_color = colors.get(color.lower())
					if new_color:
						svg_str = svg_str[:m.start()] + new_color + svg_str[m.end():]
			with open('{}/dark/{}.svg'.format(out_path, name_only), 'w') as dark_svg:
				dark_svg.write(svg_str)



with open("hashes", "w") as f:
	for (k,v) in hashes.items():
		f.write("%s %s\n" % (k, v))
