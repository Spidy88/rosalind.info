def calculate_dom_prob(hom_dom, hetero, hom_rec):
    total = hom_dom + hetero + hom_rec

    p_hom_dom__hom_dom = (hom_dom / total) * ((hom_dom-1) / (total-1))
    p_hom_dom__hetero = (hom_dom / total) * (hetero / (total-1))
    p_hom_dom__hom_rec = (hom_dom / total) * (hom_rec / (total-1))
    p_hetero__hetero = (hetero / total) * ((hetero-1) / (total-1))
    p_hetero__hom_rec = (hetero / total) * (hom_rec / (total-1))
    # p_hom_rec__hom_rec = (hom_rec / total) * ((hom_rec-1) / (total-1))

    # We multiply some probabilities by 2 to account for complement. p_A_B ==> p_B_A
    prob_100 = (p_hom_dom__hom_dom + p_hom_dom__hetero*2 + p_hom_dom__hom_rec*2)
    prob_075 = (p_hetero__hetero) * 0.75
    prob_050 = (p_hetero__hom_rec*2) * 0.5
    
    # We can skip prob_000 since it'll be multiplied by zero and not alter the final result
    # prob_000 = (p_hom_rec__hom_rec) * 0

    return prob_100 + prob_075 + prob_050

if __name__ == '__main__':
    values = input('Enter k, m, and n: ')
    hom_dom, hetero, hom_rec = [int(v) for v in values.split()]
    
    prob_dom = calculate_dom_prob(hom_dom, hetero, hom_rec)

    print('{}'.format(prob_dom))