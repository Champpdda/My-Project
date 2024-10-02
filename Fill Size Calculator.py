def calculate_image_file_size(width, height, bits_per_pixel):
    """
    คำนวณขนาดของไฟล์ภาพในหน่วยเมกะไบต์ (MB)
    :param width: ความกว้างของภาพ (พิกเซล)
    :param height: ความสูงของภาพ (พิกเซล)
    :param bits_per_pixel: ขนาดบิตต่อพิกเซล (เช่น 24 สำหรับ RGB)
    :return: ขนาดของไฟล์ภาพในเมกะไบต์ (MB)
    """
    size_bytes = (width * height * bits_per_pixel) / 8
    size_mb = size_bytes / (1024 * 1024)
    return size_mb

def calculate_video_file_size(bitrate_mbps, duration_seconds):
    """
    คำนวณขนาดของไฟล์วิดีโอในหน่วยเมกะไบต์ (MB)
    :param bitrate_mbps: บิตเรต (Megabits per second)
    :param duration_seconds: ระยะเวลา (วินาที)
    :return: ขนาดของไฟล์วิดีโอในเมกะไบต์ (MB)
    """
    size_bytes = (bitrate_mbps * 1_000_000 * duration_seconds) / 8
    size_mb = size_bytes / (1024 * 1024)
    return size_mb

def calculate_film_file_size(width, height, frames, bits_per_pixel):
    """
    คำนวณขนาดของไฟล์ฟิล์มในหน่วยกิกะไบต์ (GB)
    :param width: ความกว้างของภาพ (พิกเซล)
    :param height: ความสูงของภาพ (พิกเซล)
    :param frames: จำนวนเฟรม
    :param bits_per_pixel: ขนาดบิตต่อพิกเซล (เช่น 24 สำหรับ RGB)
    :return: ขนาดของไฟล์ฟิล์มในกิกะไบต์ (GB)
    """
    size_bytes = (width * height * frames * bits_per_pixel) / 8
    size_gb = size_bytes / (1024 * 1024 * 1024)
    return size_gb

def main():
    while True:
        print("\nSelect mode:")
        print("1. Image File Size")
        print("2. Video File Size")
        print("3. Film File Size")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            width = int(input("Enter width (pixels): "))
            height = int(input("Enter height (pixels): "))
            bits_per_pixel = int(input("Enter bits per pixel (e.g., 24 for RGB): "))
            size_mb = calculate_image_file_size(width, height, bits_per_pixel)
            print(f"Image file size: {size_mb:.2f} MB")

        elif choice == '2':
            bitrate_mbps = float(input("Enter bitrate (Mbps): "))
            duration_seconds = int(input("Enter duration (seconds): "))
            size_mb = calculate_video_file_size(bitrate_mbps, duration_seconds)
            print(f"Video file size: {size_mb:.2f} MB")

        elif choice == '3':
            width = int(input("Enter width (pixels): "))
            height = int(input("Enter height (pixels): "))
            frames = int(input("Enter number of frames: "))
            bits_per_pixel = int(input("Enter bits per pixel (e.g., 24 for RGB): "))
            size_gb = calculate_film_file_size(width, height, frames, bits_per_pixel)
            print(f"Film file size: {size_gb:.2f} GB")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
