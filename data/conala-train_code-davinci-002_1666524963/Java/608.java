String[] sentences = text.split("\\.");
StringBuilder sb = new StringBuilder();
for (int i = 0; i < sentences.length && i < maxSentences; i++) {
    sb.append(sentences[i]);
    if (i < sentences.length - 1) {
        sb.append(".");
    }
}