function write_general_matrix(file, matrix, precision, delimiter, line_terminator)
format = [create_fmt(precision, delimiter, size(matrix, 2)) line_terminator];
fid = fopen(file, 'w');
fprintf(fid, format, matrix');
fclose(fid);
end
