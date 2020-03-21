import re

def check_list_end(in_list, i):
    if in_list:
        i += '</ul>'
        in_list = False
    return in_list, i

def format_askerisks(in_list, i):
    m = re.match(r'\* (.*)', i)
    if m:
        curr = m.group(1)
        if not in_list:
            i = '<ul><li>' + curr + '</li>'
            in_list = True
        else:
            i = '<li>' + curr + '</li>'
    else:
        in_list, i = check_list_end(in_list, i)
    return in_list, i
    
def format_hashes(i):
    header_match = re.match(r'(#+) (.*)', i)
    if header_match:
        i = '<h{0}>{1}</h{0}>'.format(len(header_match.group(1)), header_match.group(2))
    return i

def format_paragraphs(i):
    if not i.startswith(("<h", "<ul", "<p", "<li")):
       i = '<p>' + i + '</p>' 
    return i
    
def format_bold(i):
    m = re.match('(.*)__(.*)__(.*)', i)
    if m:
        i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
    return i

def format_italics(i):
    m = re.match('(.*)_(.*)_(.*)', i)
    if m:
        i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
    return i

def parse_markdown(markdown):
    result = []
    in_list = False

    for i in markdown.splitlines():
        in_list, i = format_askerisks(in_list, i)
        i = format_hashes(i)
        i = format_paragraphs(i)
        i = format_bold(i)
        i = format_italics(i)
        result.append(i)
    in_list, result = check_list_end(in_list, result)
    return ''.join(result)
