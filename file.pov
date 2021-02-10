#version 3.6
#include "colors.inc"



global_settings {
	assumed_gamma 1.0
}
camera {
	location <100,50,50>
	right x*image_width/image_height
	angle 90
	look_at <-5,25,0>
}
plane {
	y,
	0 pigment {
		White
	}
}
sphere {
	<0,25,-30>,
	25
	texture {
		pigment {
			spiral1 1 color_map {
				[0.0 White]
				[0.2 Wheat]
				[0.4 Orange]
				[0.4 Clear]
				[1.0 Clear]
	 		}
			scale 5
	 	}
		normal {
			bumps 0.3 scale 0.2
		}
	}
	interior_texture {
		pigment {
	 		spiral1 1 color_map {
				[0.0 Blue]
				[0.2 Red]
				[0.6 YellowGreen]
				[0.6 Clear]
				[1.0 Clear]
			}
			scale 5
		}
		normal {
			bumps .3 scale .2
		}
	}
}
sphere {
	<0,25,30>,
	25
	texture {
		pigment {
			rgb <0.5,0.4,1>
		}
	}
	interior_texture {
		pigment {
			rgb <1,0.7,0.0>
		}
		normal {
			bumps 0.7 scale 0.15
		}
	}
	clipped_by {
		box {
			<-50,20,-50>,
			<50,35,50> inverse
		}
	}
}
light_source {
	<400,5000,3000> Red*0.5
}
fog {
	Cyan distance 1000
}
