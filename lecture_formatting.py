import json
from datetime import datetime
import os
import re
import urllib.parse

lecture_dates6100A = {
    "lecture1": "10/24/2022 15:00:00",
    "lecture2": "10/26/2022 15:00:00",
    "lecture3": "10/31/2022 15:00:00",
    "lecture4": "11/02/2022 15:00:00",
    "lecture5": "11/07/2022 15:00:00",
    "lecture6": "11/09/2022 15:00:00",
    "lecture7": "11/14/2022 15:00:00",
    "lecture8": "11/16/2022 15:00:00",
    "lecture9": "11/21/2022 15:00:00",
    "lecture10": "11/28/2022 15:00:00",
    "lecture11": "11/30/2022 15:00:00",
    "lecture12": "12/05/2022 15:00:00",
    "lecture13": "12/07/2022 15:00:00",
    "lecture14": "12/12/2022 15:00:00",
    "lecture15": "12/14/2022 15:00:00"
}

lecture_dates6100L = {
    "lecture1": "09/07/2022 15:00:00",
    "lecture2": "09/12/2022 15:00:00",
    "lecture3": "09/14/2022 15:00:00",
    "lecture4": "09/19/2022 15:00:00",
    "lecture5": "09/21/2022 15:00:00",
    "lecture6": "09/26/2022 15:00:00",
    "lecture7": "09/28/2022 15:00:00",
    "lecture8": "10/03/2022 15:00:00",
    "lecture9": "10/05/2022 15:00:00",
    "lecture10": "10/12/2022 15:00:00",
    "lecture11": "10/17/2022 15:00:00",
    "lecture12": "10/19/2022 15:00:00",
    "lecture13": "10/24/2022 15:00:00",
    "lecture14": "10/26/2022 15:00:00",
    "lecture15": "10/31/2022 15:00:00",
    "lecture16": "11/02/2022 15:00:00",
    "lecture17": "11/07/2022 15:00:00",
    "lecture18": "11/09/2022 15:00:00",
    "lecture19": "11/14/2022 15:00:00",
    "lecture20": "11/16/2022 15:00:00",
    "lecture21": "11/21/2022 15:00:00",
    "lecture22": "11/28/2022 15:00:00",
    "lecture23": "11/30/2022 15:00:00",
    "lecture24": "12/05/2022 15:00:00",
    "lecture25": "12/07/2022 15:00:00",
    "lecture26": "12/12/2022 15:00:00"
}

lecture_mapping = {
    "lecture1": "Lecture 1",
    "lecture2": "Lecture 2",
    "lecture3": "Lecture 3",
    "lecture4": "Lecture 4",
    "lecture5": "Lecture 5",
    "lecture6": "Lecture 6",
    "lecture7": "Lecture 7",
    "lecture8": "Lecture 8",
    "lecture9": "Lecture 9",
    "lecture10": "Lecture 10",
    "lecture11": "Lecture 11",
    "lecture12": "Lecture 12",
    "lecture13": "Lecture 13",
    "lecture14": "Lecture 14",
    "lecture15": "Lecture 15",
    "lecture16": "Lecture 16",
    "lecture17": "Lecture 17",
    "lecture18": "Lecture 18",
    "lecture19": "Lecture 19",
    "lecture20": "Lecture 20",
    "lecture21": "Lecture 21",
    "lecture22": "Lecture 22",
    "lecture23": "Lecture 23",
    "lecture24": "Lecture 24",
    "lecture25": "Lecture 25",
    "lecture26": "Lecture 26"
}

def get_status(current_date="10/24/2022"):
    current_date = datetime.strptime(current_date, "%m/%d/%Y")
    seen = set()
    for lecture,date in lecture_dates6100L.items():
        date = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
        if date < current_date:
            seen.add(lecture)
    return seen

def create_lectures_dict(seen, slides_path="6100L_LectureSlidesJson", transcripts_path="6100L_LectureTranscriptJSON"):
    seen_lectures = {}
    unseen_lectures = {}
    for filename in os.listdir(slides_path):
        if filename.endswith(".json"):
            file_path = os.path.join(slides_path, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                formatted_data = []
                for item in data:
                    for slide, content in item.items():
                        formatted_data.append({"slide": slide, "content": content})
                lecture = filename.split("_")[0]
                if lecture in seen:
                    seen_lectures[lecture] = {"slides": formatted_data, "lecture": lecture}
                else:
                    unseen_lectures[lecture] = {"slides": formatted_data, "lecture": lecture}

    for filename in os.listdir(transcripts_path):
        if filename.endswith(".json"):
            file_path = os.path.join(transcripts_path, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                content = ""
                for transcript in data:
                    content += f"{transcript['content']} "
                lecture = filename.split("_")[0]
                if lecture in seen:
                    seen_lectures[lecture]["transcript"] = content
                else:
                    unseen_lectures[lecture]["transcript"] = content
    return seen_lectures, unseen_lectures


def create_lecture_markdown(lecture, folder="."):
    filename = folder + f"/{lecture['lecture']}.md"
    with open(filename, 'w') as file:
        file.write(f"#{lecture['lecture']}\n\n")
        file.write(f"##SLIDES\n\n")
        for slide in lecture["slides"]:
            file.write(f"###{slide['slide']}\n")
            file.write(f"{slide['content']}\n\n")
        file.write(f"##TRANSCRIPT\n\n")
        file.write(f"{lecture['transcript']}\n")


def create_documents(seen):
    seen_lectures, unseen_lectures = create_lectures_dict(seen)
    seen_folder, all_folder = "./seen", "./all"
    if not os.path.exists(seen_folder):
        os.makedirs(seen_folder)
        os.makedirs(all_folder)
    else:
        for filename in os.listdir(seen_folder):
            file_path = os.path.join(seen_folder, filename)
            os.unlink(file_path)
        for filename in os.listdir(all_folder):
            file_path = os.path.join(all_folder, filename)
            os.unlink(file_path)
    for lecture in seen_lectures:
        create_lecture_markdown(seen_lectures[lecture], seen_folder)
        create_lecture_markdown(seen_lectures[lecture], all_folder)
    for lecture in unseen_lectures:
        create_lecture_markdown(unseen_lectures[lecture], all_folder)
    return seen_lectures, unseen_lectures

def replace_newline(obj):
    if isinstance(obj, str):
        return obj.replace("\n", "\n")
    return obj
def create_questions(questions_path="6100L_fall2022_piazza_conversations"):
    questions = []
    for filename in os.listdir(questions_path):
        if filename.endswith(".json"):
            _id = filename.split("_")[1].split(".json")[0]
            file_path = os.path.join(questions_path, filename)
            with open(file_path, "r") as file:
                data = json.load(file)
                if data[0]["type"] == "note" or len(data) < 2:
                    continue
                question =  f'Subject: {data[0]["subject"]}\n. {data[0]["content"]}'
                answer = ""
                if data[1]["type"] == "s_answer" or data[1]["type"] == "i_answer":
                    for content in data[1:]:
                        answer += f'{content["content"]}\n'
                else:
                    continue
                questions.append({"question" : question, "answer": answer, "_id" :_id })
    with open("questions6100L.json", 'w') as file:
        json.dump(questions, file, indent=4, default=replace_newline)
    
def update_piazza(directory="6100L_fall2022_piazza_conversations"):
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            # Extract the _id from the filename
            _id = filename.split("_")[1].split(".json")[0]

            # Load the JSON data from the file
            with open(os.path.join(directory, filename), 'r') as file:
                data = json.load(file)

            # Append _id to each object in the list
            for obj in data:
                obj['_id'] = _id

            # Save the modified JSON data back to the file
            with open(os.path.join(directory, filename), 'w') as file:
                json.dump(data, file, indent=4)
    
L_ids = ["l8uz5i12wve448", "lar4fh7orrd4um"]
L_ids_pics = ["l9xbpgdufew7fj"]
A_ids = ["l8avmkr2rkf2fr", "l8f1e233pwo5ko", "l8fae0knahr6hi","l8g7ge0gpk32bn", "l8hql52jjek4ap", "l8huqoy33j424q", "l8jcm4y4fq42b4", "l8jwjjfd8io6qb", "l8ovdkooveo1u5", "l8qc4lj1t1s7pq", "l8qlcwc7u81564", "l8rl3frsor61k8" , "l8rv8cdb6kw7lb (no hw)", "l8vpmtrvp4l3hf", "l9abzxho2kk40a", "l9b13ytgojn2kv", "l9czhcou4zllg", "l9de7krb8dn22n", "l9djk75rks462e", "l9dqsat0wdv4m4", "l9e9o2dcwgo7cj", "l9efh7niqwx2qf"] #first one is from homework, not lecture
A_ids_pics = ["l8hoi7jzu5f6r9", "l8hw6ohw95h4l7", "l8j1yq2ms2w1as", "l8j4jv9lkh61zz","l8ooi7r9v137ag", "l8t66ycsutn268", "l8tkzz5bet75xk", "l8vweuf33wj4im", "l9bm2njgaje766", "l9ez72a1swx6zy"]
def get_s3_url(img_tag):
    # Extract the src attribute value from the img tag
    src_match = re.search(r'src="(.*?)"', img_tag)
    if src_match:
        src = src_match.group(1)
        # Remove the leading "/redirect/s3?" part
        query_string = src.replace("/redirect/s3?", "")

        # Parse the query string to get the bucket and prefix values
        params = urllib.parse.parse_qs(query_string)
        bucket = params.get("bucket", [""])[0]
        prefix = params.get("prefix", [""])[0]

        # Decode the prefix value
        decoded_prefix = urllib.parse.unquote(prefix)

        # Construct the S3 URL
        s3_url = f"https://{bucket}.s3.amazonaws.com/{decoded_prefix}"

        return s3_url
    return None

def extract_s3_urls(text):
    # Find all <img> tags in the text using regex
    img_tags = re.findall(r'<img.*?>', text)

    # Extract S3 URLs from each <img> tag
    s3_urls = []
    for tag in img_tags:
        url = get_s3_url(tag)
        if url:
            s3_urls.append(url)
    return s3_urls