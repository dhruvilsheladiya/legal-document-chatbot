from rouge import Rouge # type: ignore
from nltk.translate.bleu_score import sentence_bleu

def evaluate_summary(generated_summary, reference_summary):
    """Compute ROUGE and BLEU scores."""
    rouge = Rouge()
    rouge_score = rouge.get_scores(generated_summary, reference_summary)[0]

    bleu_score = sentence_bleu([reference_summary.split()], generated_summary.split())

    return {"rouge": rouge_score, "bleu": bleu_score}
