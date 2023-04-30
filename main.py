import recent_earthquake_detection

if __name__ == '__main__':
    print('Main Application')
    result = recent_earthquake_detection.ekstraksi_data()
    recent_earthquake_detection.tampilkan_data(result)
