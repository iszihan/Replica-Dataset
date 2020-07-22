import argparse 
import os

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--videos", type=str, nargs="+", default="cafe")
	parser.add_argument("--poses", type=str, nargs="+", default="box3")
	parser.add_argument("--op",type=str, default="render",help='[render, stitch, all]')
	args=parser.parse_args()
	
	videos = args.videos[0].split(" ")
	poses = args.poses[0].split(" ")
	for v in videos:
		for pose in poses:
			output_dir = "assets/%s_output/%s/" % (v, pose)
			if args.op == 'render' or args.op == 'all':
				for f in range(3):
					if not os.path.isdir(output_dir): os.mkdir(output_dir)
					command_line = './build/ReplicaSDK/DepthMeshRendererLayeredBatch assets/%s/test_data_layered assets/%s_poses.txt %s n 480 270 %d %d' % (v, pose, output_dir, f*100+1, (f+1)*100+1) 
					print(command_line)
					os.system(command_line)
			if args.op == 'stitch':
				command_line = 'ffmpeg -r 30 -f image2 -s 480x270 -i %s/out_%%04d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p assets/%s_output/%s.mp4' % (output_dir, v, pose)
				os.system(command_line)
				print(command_line)			
	
