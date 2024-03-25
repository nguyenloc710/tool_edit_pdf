import os
import threading
from pathlib import Path
from typing import Union, Literal, List

from PyPDF2 import PdfWriter, PdfReader


def create_directory(path):
    directory = Path(path)
    if not directory.is_dir():
        directory.mkdir(parents=True)


def stamp(
        content_pdf: Path,
        stamp_pdf: Path,
        pdf_result: Path,
        page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    create_directory(Path(pdf_result).parent)  # Create the directory if it doesn't exist
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[0]

    writer = PdfWriter()

    reader = PdfReader(content_pdf)
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))
    for i in page_indices:
        for turn in range(3):
            try:
                content_page = reader.pages[i]
                content_page.mergeTranslatedPage(image_page,
                                                 (float(content_page.mediaBox[2]) - (
                                                         float(content_page.mediaBox[2]) * 0.35)),
                                                 (float(content_page.mediaBox[3]) - (
                                                         float(content_page.mediaBox[3]) * 0.33)))
                if content_page.mediaBox.width > content_page.mediaBox.height:
                    content_page.mergeTranslatedPage(image_page,
                                                     (float(content_page.mediaBox[2]) - (
                                                             float(content_page.mediaBox[2]) * 0.35)),
                                                     (float(content_page.mediaBox[3]) - (
                                                             float(content_page.mediaBox[3]) * 0.45)))
                writer.add_page(content_page)
                break
            except Exception as e:
                log_text = f"{content_pdf} :ERROR: {str(e)}"
                with open(log_error_path, "w") as file_log:
                    file_log.write(log_text + '\n')

    with open(pdf_result, "wb") as fp:
        writer.write(fp)


def get_all_files_in_folder(folder_path):
    file_paths = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file).replace("\\", "/"))
    return file_paths


path_source_file = "C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM/"
path_folder_save_file = "C:/CFM/DE/account-statistic-service-anh-hieu/CarEditPDF-TEST/"
log_error_path = "error.txt"
if __name__ == "__main__":
    path_files = get_all_files_in_folder("C:/CFM/DE/account-statistic-service-anh-hieu/CarDoctor AutoISM/TOYOTA/Camry/2006-2009/2006-2009/Location&Routing/GroundPoints")
    threading_path_files = []
    count = 1
    for index, path_file in enumerate(path_files):
        print(index)
        threading_path_files.append(path_file)
        if count % 10 == 0:
            t1 = threading.Thread(
                target=stamp(threading_path_files[0], "logo.pdf",
                             threading_path_files[0].replace(path_source_file, path_folder_save_file)), name='t1')
            t2 = threading.Thread(
                target=stamp(threading_path_files[1], "logo.pdf",
                             threading_path_files[1].replace(path_source_file, path_folder_save_file)), name='t2')
            t3 = threading.Thread(
                target=stamp(threading_path_files[2], "logo.pdf",
                             threading_path_files[2].replace(path_source_file, path_folder_save_file)), name='t3')
            t4 = threading.Thread(
                target=stamp(threading_path_files[3], "logo.pdf",
                             threading_path_files[3].replace(path_source_file, path_folder_save_file)), name='t4')
            t5 = threading.Thread(
                target=stamp(threading_path_files[4], "logo.pdf",
                             threading_path_files[4].replace(path_source_file, path_folder_save_file)), name='t5')
            t6 = threading.Thread(
                target=stamp(threading_path_files[5], "logo.pdf",
                             threading_path_files[5].replace(path_source_file, path_folder_save_file)), name='t6')
            t7 = threading.Thread(
                target=stamp(threading_path_files[6], "logo.pdf",
                             threading_path_files[6].replace(path_source_file, path_folder_save_file)), name='t7')
            t8 = threading.Thread(
                target=stamp(threading_path_files[7], "logo.pdf",
                             threading_path_files[7].replace(path_source_file, path_folder_save_file)), name='t8')
            t9 = threading.Thread(
                target=stamp(threading_path_files[8], "logo.pdf",
                             threading_path_files[8].replace(path_source_file, path_folder_save_file)), name='t9')
            t10 = threading.Thread(
                target=stamp(threading_path_files[8], "logo.pdf",
                             threading_path_files[8].replace(path_source_file, path_folder_save_file)), name='t10')
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            t8.join()
            t9.join()
            t10.join()
            count = 0
            threading_path_files = []
        count += 1
    try:
        t1 = threading.Thread(
            target=stamp(threading_path_files[0], "logo.pdf",
                         threading_path_files[0].replace(path_source_file, path_folder_save_file)), name='t1')
        t2 = threading.Thread(
            target=stamp(threading_path_files[1], "logo.pdf",
                         threading_path_files[1].replace(path_source_file, path_folder_save_file)), name='t2')
        t3 = threading.Thread(
            target=stamp(threading_path_files[2], "logo.pdf",
                         threading_path_files[2].replace(path_source_file, path_folder_save_file)), name='t3')
        t4 = threading.Thread(
            target=stamp(threading_path_files[3], "logo.pdf",
                         threading_path_files[3].replace(path_source_file, path_folder_save_file)), name='t4')
        t5 = threading.Thread(
            target=stamp(threading_path_files[4], "logo.pdf",
                         threading_path_files[4].replace(path_source_file, path_folder_save_file)), name='t5')
        t6 = threading.Thread(
            target=stamp(threading_path_files[5], "logo.pdf",
                         threading_path_files[5].replace(path_source_file, path_folder_save_file)), name='t6')
        t7 = threading.Thread(
            target=stamp(threading_path_files[6], "logo.pdf",
                         threading_path_files[6].replace(path_source_file, path_folder_save_file)), name='t7')
        t8 = threading.Thread(
            target=stamp(threading_path_files[7], "logo.pdf",
                         threading_path_files[7].replace(path_source_file, path_folder_save_file)), name='t8')
        t9 = threading.Thread(
            target=stamp(threading_path_files[8], "logo.pdf",
                         threading_path_files[8].replace(path_source_file, path_folder_save_file)), name='t9')
        t10 = threading.Thread(
            target=stamp(threading_path_files[8], "logo.pdf",
                         threading_path_files[8].replace(path_source_file, path_folder_save_file)), name='t10')
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()
        t8.start()
        t9.start()
        t10.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t8.join()
        t9.join()
        t10.join()
    except Exception as e:
        print("Done")