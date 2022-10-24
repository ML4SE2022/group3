def penrose(depth):
    print('''<svg viewBox="-100 -100 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
	<path id="A0" d="M 80.90169943749474 58.778525229247315 L 0 0 100 0" stroke="black" fill="#8bc" />
	<path id="B0" d="M 0 0 80.90169943749474 58.778525229247315 161.80339887498948 0" stroke="black" fill="#97e" />''')

    for d in range(depth):
        print(f'''	<g id="A{d+1}" transform="translate(100, 0) scale(0.6180339887498949)">
		<use href="#A{d}" transform="rotate(108)" />
		<use href="#B{d}" transform="scale(-1, 1)" />
	</g>
	<g id="B{d+1}">
		<use href="#A{d+1}" />
		<use href="#B{d}" transform="translate(100, 0) scale(0.6180339887498949) rotate(144) translate(-80.90169943749474,-58.778525229247315)"/>
	</g>''')

    print(f'''	<g id="G">
		<use href="#A{d+1}"/>
		<use href="#A{d+1}" transform="scale(1, -1)" />
	</g>
  </defs>
  <g transform="scale(2, 2)">
	<use href="#G" transform="rotate(-144)" />
	<use href="#G" transform="rotate(-72)" />
	<use href="#G" transform="rotate(0)" />
	<use href="#G" transform="rotate(72)" />
	<use href="#G" transform="rotate(144)" />
  </g>
</svg>''')

penrose(6)