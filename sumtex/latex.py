import re


def process_latex_file(path, split_at="section"):
    with open(path, 'r') as file:
        raw_data = file.read()

    tmp_data = raw_data
    tmp_data = tmp_data[:tmp_data.find(r"\appendix")]
    tmp_data = tmp_data[:tmp_data.find(r"\end{document}")]

    tmp_data = re.sub(r'\\cite\{([^}]*)\}', '', tmp_data)
    tmp_data = re.sub(r'\\label\{([^}]*)\}', '', tmp_data)
    tmp_data = re.sub(r'\\begin{align}([^}]*)\\end{align}', '', tmp_data, flags=re.DOTALL)
    tmp_data = re.sub(r'\\begin{pyin}([^}]*)\\end{pyin}', '', tmp_data, flags=re.DOTALL)
    tmp_data = re.sub(r'^%.*\n?', '', tmp_data, flags=re.MULTILINE)

    for format_name in ["texttt", "textbf", "textit"]:
        tmp_data = re.sub(rf'\\{format_name}{{([^}}]*)}}', '\\1', tmp_data)

    section_starts = [i for i in range(len(tmp_data)) if tmp_data.startswith(rf"\{split_at}{{", i)]
    section_starts.append(-1)

    sections = {}

    for start, stop in zip(section_starts[:-1], section_starts[1:]):
        section_text = tmp_data[start:stop]
        section_title = re.search(rf'\\{split_at}\{{([^}}]*)\}}', section_text).group(1).strip()

        for sec_name in ["section", "subsection", "paragraph"]:
            section_text = re.sub(rf'\\{sec_name}{{([^}}]*)}}', '\\1', section_text)

        sections[section_title] = section_text

    return sections
