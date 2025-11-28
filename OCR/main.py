import os

from magic_pdf.data.data_reader_writer import FileBasedDataWriter, FileBasedDataReader
from magic_pdf.data.dataset import PymuDocDataset
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.config.enums import SupportedPdfParseMethod


def process_pdf(pdf_file_path, local_image_dir, local_md_dir):
    try:
        # 提取文件名（不含扩展名）
        name_without_suff = os.path.basename(pdf_file_path).split(".")[0]
        print(name_without_suff)

        # 准备环境
        image_dir = str(os.path.basename(local_image_dir))
        os.makedirs(local_image_dir, exist_ok=True)

        image_writer, md_writer = FileBasedDataWriter(local_image_dir), FileBasedDataWriter(
            local_md_dir
        )

        # 读取 PDF 文件内容
        reader1 = FileBasedDataReader("")
        pdf_bytes = reader1.read(pdf_file_path)

        # 创建数据集实例
        ds = PymuDocDataset(pdf_bytes)

        # 推理
        if ds.classify() == SupportedPdfParseMethod.OCR:
            infer_result = ds.apply(doc_analyze, ocr=True)
            pipe_result = infer_result.pipe_ocr_mode(image_writer)
        else:
            infer_result = ds.apply(doc_analyze, ocr=False)
            pipe_result = infer_result.pipe_txt_mode(image_writer)

        # 绘制模型结果
        infer_result.draw_model(os.path.join(local_md_dir, f"{name_without_suff}_model.pdf"))

        # 获取模型推理结果
        model_inference_result = infer_result.get_infer_res()

        # # 绘制布局结果
        # pipe_result.draw_layout(os.path.join(local_md_dir, f"{name_without_suff}_layout.pdf"))
        #
        # # 绘制跨度结果
        # pipe_result.draw_span(os.path.join(local_md_dir, f"{name_without_suff}_spans.pdf"))

        # 获取 Markdown 内容
        md_content = pipe_result.get_markdown(image_dir)

        # 保存 Markdown 文件
        pipe_result.dump_md(md_writer, f"{name_without_suff}.md", image_dir)

        # 获取内容列表
        content_list_content = pipe_result.get_content_list(image_dir)

        # 保存内容列表
        pipe_result.dump_content_list(md_writer, f"{name_without_suff}_content_list.json", image_dir)

        # # 获取中间 JSON 内容
        # middle_json_content = pipe_result.get_middle_json()
        #
        # # 保存中间 JSON 文件
        # pipe_result.dump_middle_json(md_writer, f'{name_without_suff}_middle.json')

        print(f"处理完成: {pdf_file_path}")
    except Exception as e:
        print(f"处理 {pdf_file_path} 时出错: {e}")


def process_all_pdfs_in_folder(folder_path, local_image_dir, local_md_dir):
    if not os.path.exists(folder_path):
        print(f"文件夹 {folder_path} 不存在。")
        return

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_file_path = os.path.join(root, file)
                print(pdf_file_path)
                process_pdf(pdf_file_path, local_image_dir, local_md_dir)


# 配置参数
pdf_folder = ""  # 替换为实际的 PDF 文件夹路径
local_image_dir, local_md_dir = "output/images", "output"

# 处理文件夹中的所有 PDF 文件
process_all_pdfs_in_folder(pdf_folder, local_image_dir, local_md_dir)