import SimpleITK as sitk
import matplotlib.pyplot as plt

def preprocess_image(input_path, output_path): 
    image = sitk.ReadImage(input_path) # Read the image
    image = sitk.RescaleIntensity(image) # Normalize the intensity value of the image
    image = sitk.Shrink(image, [2, 2, 2]) # Downsample the image by a factor of [2, 2, 2] in each dimension
    sitk.WriteImage(image, output_path) # Save the pre-processed image to specified output path
    print(f"Processed: {input_path} -> {output_path}") # Logs the completion of image pre-processing

    # Load input and output images
    input_image = sitk.ReadImage(input_path)
    output_image = sitk.ReadImage(output_path)

    # Convert to numpy arrays for visualization
    input_array = sitk.GetArrayViewFromImage(input_image)
    output_array = sitk.GetArrayViewFromImage(output_image)

    # Display middle slices
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Input Image (Slice)")
    plt.imshow(input_array[input_array.shape[0] // 2], cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title("Output Image (Slice)")
    plt.imshow(output_array[output_array.shape[0] // 2], cmap='gray')
    plt.show()

if __name__ == "__main__":
    preprocess_image("data/manifest-1732601339123/ReMIND/ReMIND-001/12-25-1982-NA-Preop-56579/303.000000-tumor seg - MR ref 3DSAGT2SPACE-20521/1-1.dcm", "data/preprocessed/0001.dcm")
    preprocess_image("data/manifest-1732601339123/ReMIND/ReMIND-001/12-25-1982-NA-Preop-56579/301.000000-cerebrum seg - MR ref 3DAXT1postcontrast-23103/1-1.dcm", "data/preprocessed/0002.dcm")
    preprocess_image("data/manifest-1732601339123/ReMIND/ReMIND-001/12-25-1982-NA-Preop-56579/300.000000-ventricles seg - MR ref 3DAXT1postcontrast-54539/1-1.dcm", "data/preprocessed/0002.dcm")