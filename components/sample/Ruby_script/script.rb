require 'fileutils'

text_path = ARGV[0]
pattern = ARGV[1]
filtered_text_path = ARGV[2]

regex = Regexp.new(pattern)

# Create the directory for the output file if it doesn't exist
FileUtils.mkdir_p(File.dirname(filtered_text_path))

# Open the input file for reading
File.open(text_path, 'r') do |reader|
  # Open the output file for writing
  File.open(filtered_text_path, 'w') do |writer|
    reader.each_line do |line|
      if regex.match(line)
        writer.write(line)
      end
    end
  end
end
