# -*- mode: Python -*-

BAZEL_SOURCES_CMD_TEMPLATE = """
  bazel query 'filter("^//", kind("source file", deps(set(%s))))' --order_output=no
  """.strip()

def bazel_labels_to_files(labels):
  files = {}
  for l in labels:
    if l.startswith("//external/") or l.startswith("//external:"):
      continue
    elif l.startswith("//"):
      l = l[2:]

    path = l.replace(":", "/")

    # if not path.startswith("/"):
    #   path = "/{}".format(path)
    if path.startswith("/"):
      path = path[1:]

    path = '../../{}'.format(path)

    files[path] = None

  return files.keys()

def bazel_sourcefile_deps(target):
  return bazel_labels_to_files(str(local(BAZEL_SOURCES_CMD_TEMPLATE % target)).splitlines())


def extract_apps_libs_directories(file_paths):
    directories = {}
    for file_path in file_paths:
        # Get the directory component of the file path
        # replacing relative prefix from bazel_labels_to_files
        directory = os.path.dirname(file_path).replace('../../', '', 1)

        # Split the directory path into individual directories
        split_dirs = directory.split('/')

        # Get the first two directories
        first_two_dirs = os.path.join('/', *split_dirs[:2])

        # Append the result to the list of directories
        directories[first_two_dirs] = True

    return directories.keys()




def create_id_to_fragment_mapping(path_fragments):
    id_to_fragment_mapping = {}

    for path_fragment in path_fragments:
        id_to_fragment_mapping[path_fragment["id"]] = path_fragment

    return id_to_fragment_mapping

def build_path_from_id(id_to_fragment_mapping, current_id):
    path_fragment = id_to_fragment_mapping[current_id]
    label = path_fragment["label"]

    if "parentId" not in path_fragment:
        return label

    parent_path = build_path_from_id(id_to_fragment_mapping, path_fragment["parentId"])
    return os.path.join(parent_path, label)
