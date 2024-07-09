"""
This file contains the necessary components for decoding and encoding files.
"""
import cv2
import numpy as np
import warnings
"""
Holds the metadata to append to a video as the first frame so the decoder knows what to do.
"""
class MetaData:
    def __init__(self, file_name, file_ext, color_depth, res):
        self.file_name = file_name
        self.file_ext = file_ext
        self.color_depth = color_depth
        self.res = res

"""
Create an encoding or decoding instance
"""
class CodingInstance:

    def __init__(self):
        self.resolution = None
        self.color_depth = None
        self.infile_name = None
        self.meta_data = None
        self.block_size = None
        self.blocks_per_row = None
        self.blocks_per_col = None

    """
    Begin encoding the input file into a video.
    color_depth: number of bits used for one color channel (bpc)
    resolution: tuple containing (horizontal , vertical) pixels
    block_size: number of pixels per side of a color block
    """

    def Encode(self, infile_name, color_depth, resolution, block_size):
        self.infile_name = infile_name
        self.color_depth = color_depth
        self.resolution = resolution
        self.block_size = block_size

        input_file = open(infile_name, 'rb')
        chunk_size = self.GetBytesPerFrame()

        data = input_file.read(chunk_size)
        blocks_created = 0

        while data:
            print(data.hex())

            base_index = 0
            frame = np.zeros((self.resolution[1], self.resolution[0], 3), dtype=np.uint8)
            y = 0
            for i in range(self.blocks_per_col):
                x = 0
                for j in range(self.blocks_per_row):

                    b = data[base_index] if base_index < len(data) else 0
                    g = data[base_index + 1] if base_index + 1 < len(data) else 0
                    r = data[base_index + 2] if base_index + 2 < len(data) else 0
                    color = (b, g, r)

                    if color == (0, 0, 0):
                        # print('EXIT CONDITION ACTIVATED')
                        i = self.blocks_per_col
                        break
                    self.CreateBlock(frame, y, x, color)

                    ### DEBUG ###
                    #blocks_created += 1
                    #print('block created: ' + str(blocks_created) +
                    #      ' b: ' + str(b) +
                    #      ' g: ' + str(g) +
                    #      ' r: ' + str(r))
                    ### DEBUG ###

                    x += block_size
                    base_index += 3 # Move ahead in the data

                y += block_size
                print('moved down in y. y = ' + str(y) + ' j = ' + str(j))


            cv2.imwrite('block_image.png', frame)
            cv2.imshow('Block Image', frame)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            data = input_file.read(chunk_size)

        input_file.close()

    """
    Begin decoding the video into an output file.
    """
    def Decode(self, infile):
        None

    """
    Return the number of bits used to represent a color (log2(n) bits, where n is the total number of colors).
    Higher numbers will make the encoding algorithm more efficient at storing data, but may have issues being decoded when
        the video is run through compression (e.g. YouTube).
    """
    def GetColorDepth(self, bits_per_color):
        None
    """
    Get the total number of bytes which can be stored in a frame of video, so we can determine how much of the file to read at once.
    This number is dependent on the color depth and resolution. It also calculates the amount of blocks which can be stored per row and column.
    """
    def GetBytesPerFrame(self):
        hor = self.resolution[0]
        vert = self.resolution[1]
        block_area = pow(self.block_size, 2)
        self.blocks_per_row = hor // self.block_size

        self.blocks_per_col = vert // self.block_size

        data_per_frame = self.blocks_per_row * self.blocks_per_col * self.color_depth * 3 # The number is taken times 3 since there are 3 color channels (b, g ,r)
        max_data_per_frame = hor * vert / block_area * self.color_depth * 3

        if data_per_frame != max_data_per_frame:
            warnings.warn("The block size you have chosen is not optimal for your resolution (" +
                          str(hor) + " * " + str(vert) +
                          "). This will result in some wasted space per frame.")

        return data_per_frame

    """
    Create the starting frame of the video, which will tell us the file extension, color depth, etc.
    """
    def CreateVideoMetaData(self):
        None

    """
    Read starting frame of video to determine what settings to use when decoding.
    """
    def ReadVideoMetaData(self):
        None
    """
    Generate a single frame of the video so it can be stored to the frame list.
    """
    def GenerateFrame(self):
        None
    """
    Take the list of frames and turn them into a video.
    """
    def GenerateVideo(self):
        None

    """
    Add a number of 0s to the end of a string of bits until it reaches the color_depth * 3.
    This is for when the end of the file is reached.
    """
    def PadBits(self, bits):
        cur_length = len(bits)
        intended_length = self.color_depth * 3 # 3 channels (b, g, r)

        bits += '0' * (intended_length - cur_length)

        return bits

    """
    Create a color block given an image and its starting coordinate (top left corner)
    """
    def CreateBlock(self, image, starting_y, starting_x, color):

        for i in range(self.block_size):
            for j in range(self.block_size):
                image[starting_y + i, starting_x + j] = color


