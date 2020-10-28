import argparse
import os

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--videos", type=str, nargs="+", default="cafe")
	parser.add_argument("--poses", type=str, nargs="+", default="box3")
	parser.add_argument("--op",type=str, default="render", help='[render, stitch, all]')
	parser.add_argument("--format", type=str, default='psp', help='[psp, erp]')
	args=parser.parse_args()

	w = 512 if args.format == 'psp' else 2048
	h = 288 if args.format == 'psp' else 1024

	videos = args.videos[0].split(" ")
	poses = args.poses[0].split(" ")
	for v in videos:
		for pose in poses:
			output_dir = "assets/%s_output/%s/" % (v, pose)
			if args.op == 'render' or args.op == 'all':
				for f in range(6):
					if not os.path.isdir(output_dir): os.mkdir(output_dir)
					command_line = './build/ReplicaSDK/DepthMeshRendererLayeredBatch assets/%s/test_data_layered assets/%s/%s_%s_poses.txt %s %s %d %d %d %d' % (v, v, pose, v, output_dir, 'y' if args.format=='erp' else 'n', w, h, f*50+1, (f+1)*50+1)
					print(command_line)
					os.system(command_line)
			if args.op == 'stitch' or args.op == 'all':
				command_line = 'ffmpeg -r 20 -f image2 -s %dx%d -i %s/out_%%04d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p assets/%s_output/%s.mp4' % (w, h, output_dir, v, pose)
				os.system(command_line)
				print(command_line)
