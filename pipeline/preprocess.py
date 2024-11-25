import SimpleITK as sitk

def preprocess_image(input_path, output_path): 
    image = sitk.ReadImage(input_path) # Read the image
    image = sitk.RescaleIntensity(image) # Normalize the intensity value of the image
    image = sitk.Shrink(image, [2, 2, 2]) # Downsample the image by a factor of [2, 2, 2] in each dimension
    sitk.WriteImage(image, output_path) # Save the pre-processed image to specified output path
    print(f"Processed: {input_path} -> {output_path}") # Logs the completion of image pre-processing

if __name__ == "__main__":
    preprocess_image("data/sample.dcm", "data/preprocessed/sample_processed.dcm")
