from .cli import parser
from .algorithms import Container
from .input import FileInput
from .output import FileOutput
from .handle import FilterItems, ConvertItems

if __name__ == "__main__":
    # parsing command line arguments
    args = parser.parse_args()
    # reading data from file
    input = FileInput(path=args.input)
    data = input.read()
    # filtering out empty lines
    filter_data = FilterItems(filter_func=lambda item: True if item != "" else False)
    data = filter_data(data=data)
    # converting data to float
    to_float = ConvertItems(convert_func=lambda item: float(item))
    data = to_float(data=data)
    # sorting data
    container = Container()
    algorithm = container.algorithm(key=args.algorithm)
    sorted_data = algorithm(data=data)
    # converting sorted data to str
    to_str = ConvertItems(convert_func=lambda item: str(item))
    sorted_data = to_str(data=sorted_data)
    # writing data to file
    output = FileOutput(path=args.output)
    output.write(data=sorted_data)
