function []=wrapper(arg1)
addpath('./')
inp = readmatrix('userinput.txt')

if strcmp(arg1,'a')
  precision = '%.2f'
  output = icbm_spm2tal(inp);
elseif strcmp(arg1,'b')
  precision = '%.2f'
  output = icbm_fsl2tal(inp);
elseif strcmp(arg1,'c')
  precision = '%.2f'
  output = icbm_other2tal(inp);
elseif strcmp(arg1,'d')
  precision = '%.0f'
  output = tal2icbm_spm(inp);
elseif strcmp(arg1,'e')
  output = tal2icbm_fsl(inp);
  precison = '%.0f';
elseif strcmp(arg1,'f')
  output = tal2icbm_other(inp);
  precison = '%.0f';

end

file = 'results.dat'; % file name 
%precision = '%.0f'; % desired precision for values in A (for possible values of this parameter, see https://www.mathworks.com/help/matlab/ref/fprintf.html#btf8xsy-1_sep_shared-formatSpec)
delimiter = '	';
line_terminator = '\n';
try
  write_general_matrix(file, output, precision, delimiter, line_terminator);
catch
  warning('Failed to write matrix');
  exit
end

exit
