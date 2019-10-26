from __future__ import print_function
import os
import sys
import time
from arg_parser import parse_argments
from urllib3.exceptions import ProtocolError
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint


def string_to_byte_array(byte_string):
    tmp_str = byte_string[2:-1]
    byte_array = []

    while len(tmp_str) != 0:
        if tmp_str[0] == '\\':
            if tmp_str[1] == 'x':
                val = int(tmp_str[2:4], 16)
                tmp_str = tmp_str[4:]
            else:
                if tmp_str[1] == 'n':
                    val = ord('\n')
                elif tmp_str[1] == '\\':
                    val = ord('\\')
                elif tmp_str[1] == 't':
                    val = ord('\t')
                elif tmp_str[1] == 'r':
                    val = ord('\r')
                elif tmp_str[1] == 'f':
                    val = ord('\f')
                elif tmp_str[1] == 'b':
                    val = ord('\b')
                elif tmp_str[1] == 'a':
                    val = ord('\a')
                elif tmp_str[1] == "'":
                    val = ord("\'")
                tmp_str = tmp_str[2:]
        else:
            val = ord(tmp_str[0])
            tmp_str = tmp_str[1:]
        byte_array.append(val)
    return byte_array

def main():
    print("***Checking commandline options***")
    if len(sys.argv) != 2:
        print('Bad command argment format.')
        print('Format: python converter.py <path>')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the path to be listed')
        sys.exit()

    path = sys.argv[1]
    if not os.path.isfile(path):
        print("HEIC file not found.")
        print("Path:{}".format(path))
        sys.exit()
    else:
        print("HEIC file found.")
        print("Path:{}".format(path))

    # Configure API key authorization: Apikey
    configuration = cloudmersive_convert_api_client.Configuration()
    configuration.api_key['Apikey'] = '7ae50f10-3e26-4a08-a472-bae0f9e713d8'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['Apikey'] = 'Bearer'

    # create an instance of the API class
    api_instance = cloudmersive_convert_api_client.ConvertImageApi(
        cloudmersive_convert_api_client.ApiClient(configuration))
    format1 = 'HEIC'  # str | Input file format as a 3+ letter file extension.  You can also provide UNKNOWN for unknown file formats. Supported formats include AAI, ART, ARW, AVS, BPG, BMP, BMP2, BMP3, BRF, CALS, CGM, CIN, CMYK, CMYKA, CR2, CRW, CUR, CUT, DCM, DCR, DCX, DDS, DIB, DJVU, DNG, DOT, DPX, EMF, EPDF, EPI, EPS, EPS2, EPS3, EPSF, EPSI, EPT, EXR, FAX, FIG, FITS, FPX, GIF, GPLT, GRAY, HDR, HEIC, HPGL, HRZ, ICO, ISOBRL, ISBRL6, JBIG, JNG, JP2, JPT, J2C, J2K, JPEG/JPG, JXR, MAT, MONO, MNG, M2V, MRW, MTV, NEF, ORF, OTB, P7, PALM, PAM, PBM, PCD, PCDS, PCL, PCX, PDF, PEF, PES, PFA, PFB, PFM, PGM, PICON, PICT, PIX, PNG, PNG8, PNG00, PNG24, PNG32, PNG48, PNG64, PNM, PPM, PSB, PSD, PTIF, PWB, RAD, RAF, RGB, RGBA, RGF, RLA, RLE, SCT, SFW, SGI, SID, SUN, SVG, TGA, TIFF, TIM, UIL, VIFF, VICAR, VBMP, WDP, WEBP, WPG, X, XBM, XCF, XPM, XWD, X3F, YCbCr, YCbCrA, YUV
    format2 = 'JPG'  # str | Output (convert to this format) file format as a 3+ letter file extension.  Supported formats include AAI, ART, ARW, AVS, BPG, BMP, BMP2, BMP3, BRF, CALS, CGM, CIN, CMYK, CMYKA, CR2, CRW, CUR, CUT, DCM, DCR, DCX, DDS, DIB, DJVU, DNG, DOT, DPX, EMF, EPDF, EPI, EPS, EPS2, EPS3, EPSF, EPSI, EPT, EXR, FAX, FIG, FITS, FPX, GIF, GPLT, GRAY, HDR, HEIC, HPGL, HRZ, ICO, ISOBRL, ISBRL6, JBIG, JNG, JP2, JPT, J2C, J2K, JPEG/JPG, JXR, MAT, MONO, MNG, M2V, MRW, MTV, NEF, ORF, OTB, P7, PALM, PAM, PBM, PCD, PCDS, PCL, PCX, PDF, PEF, PES, PFA, PFB, PFM, PGM, PICON, PICT, PIX, PNG, PNG8, PNG00, PNG24, PNG32, PNG48, PNG64, PNM, PPM, PSB, PSD, PTIF, PWB, RAD, RAF, RGB, RGBA, RGF, RLA, RLE, SCT, SFW, SGI, SID, SUN, SVG, TGA, TIFF, TIM, UIL, VIFF, VICAR, VBMP, WDP, WEBP, WPG, X, XBM, XCF, XPM, XWD, X3F, YCbCr, YCbCrA, YUV
    input_file = path  # file | Input file to perform the operation on.
    try:
        # Image format conversion
        api_response = api_instance.convert_image_image_format_convert(format1, format2, input_file)
        byte_array = string_to_byte_array(api_response)

        print(byte_array)
        with open('ret.bin', 'wb') as the_file:
            file_byte_array = bytearray(byte_array)
            the_file.write(file_byte_array)

    except ApiException as e:
        print("Exception when calling ConvertImageApi->convert_image_image_format_convert: %s\n" % e)


if __name__ == '__main__':
    main()
