function irclog(q) {
	q = q.replace(/(\r\n|\r|\n)/g, "\n").split("\n");

	for (key in q) {
		val = q1[key].replace(/(\s{2,})/g, ' ');
		if (val[0] == ' ') {
			val = val.substr(1);
		}
		q2 = val.split(' ');

		if ((is_numeric(q2[0][1]) && is_numeric(q2[0][2]) && q2[0][3] == ':' && is_numeric(q2[0][4]) && is_numeric(q2[0][5])) || (is_numeric(q2[0][0]) && is_numeric(q2[0][1]) && q2[0][2] == ':' && is_numeric(q2[0][3]) && is_numeric(q2[0][4]))) {
			q2[0] = '['+q2[0].split('[').join('').split(']').join('').split('(').join('').split(')').join('')+']';
			p = 1;
		} else {
			p = 0;
		}
		if (q2[(0+p)] != '*' && q2[(0+p)] != '•' && q2[(0+p)] != '€') {
			if (q2[(0+p)] == '·' && q2[(2+p)] == '·') {
				delete q2[(0+p)];
				delete q2[(2+p)];
				q2[(1+p)] = '<'+q2[(1+p)].split('<').join('').split('>').join('').split('(').join('').split(')').join('')+'>';
			} else {
				if (q2[(1+p)] == '›') {
					q2[(1+p)] = q2[(0+p)];
					q2[(0+p)] = '*';
				} else {
					if (q2[(1+p)] == '•') {
						delete q2[(1+p)];
					}
					q2[(0+p)] = '<'+q2[(0+p)].split('<').join('').split('>').join('').split('(').join('').split(')').join('')+'>';
				}
			}
		} else {
			q2[(0+p)] = '*';
		}
		q[key] = q2.join(' ');
	}
	return q.join("\n");
}
