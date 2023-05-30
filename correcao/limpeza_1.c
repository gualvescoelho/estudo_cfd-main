#include<stdio.h>
#include<stdlib.h>

/*
	Codigo desenvolvido por Gustavo Alves Coelho, 22/03/2021
	Ajustado para apenas limpar o texto
*/

//------------------------------------------COMECO PARTE LIMPA TEXTO
struct _LETRAS_
{
	char letra;
	struct _LETRAS_ * proxima;
	struct _LETRAS_ * anterior;
};
typedef struct _LETRAS_ *letras;

void ler_caracteres();
letras add_letras(char letra, letras anterior);
letras pular_enderecos(letras aux1, char fechamento, char fechamento_2);
void retirar_letras();
void limpar_dados2(struct _LETRAS_ *lista);

struct _LETRAS_ * inicio_lista_letras, *fim_lista_letra;
struct _LETRAS_ * inicio_limpo, * fim_limpo;

void retira_parenteses(int x); //processo a ser feito apos retirar os probes ou time

void main(int argc, char *argv[])
{
	ler_caracteres("C:\\testes\\U", "C:\\testes\\saidasa.txt"); //[1] = nome do arquivo q vai ser lido, [2] arquivo de saida
	//ler_caracteres(argv[1], argv[2]); //[1] = nome do arquivo q vai ser lido, [2] arquivo de saida
	system("pause");
	return;
}

//COMECO PARTE LIMPA TEXTO
void retirar_letras(char nome_out[250])
{
	FILE *arq_out;
	struct _LETRAS_ *aux;
	aux = inicio_lista_letras;
	
	arq_out = fopen(nome_out,"w+b");
	
	while(aux->proxima != NULL)
	{	
	
		switch(aux->letra)
		{
			case '#': 
			aux = pular_enderecos(aux,'(','\n');	
			break;			
			
			case ')':
			aux = aux->proxima;
			break;
		}	
	
		if(aux->letra != '(')
		fprintf(arq_out,"%c",aux->letra);
		
		aux = aux->proxima; 		
	}
	
	fclose(arq_out);
}

letras pular_enderecos(letras aux1, char fechamento, char fechamento_2)
{
	struct _LETRAS_ *aux;
	aux = aux1; //salva o endereco que parar em aux para poder continuar
	
	while(aux->letra != fechamento && aux->letra != fechamento_2) //enquanto nao passar por o fechamento da condicao
	{
		aux = aux->proxima;
	} //sair com o endere�o apos condicao
	
	return aux;
}

void ler_caracteres(char* nome_in, char* nome_out)
{
	char letra, letra_ant, teste;
	FILE *arq_ler, *arq_saida;
	int i = 0;
	letras aux;
	
	arq_ler = fopen(nome_in,"r+b");
	
	while(!arq_ler)
	{
		printf("\n ARQUIVO U NAO ENCONTRADO, OPERACAO CANCELADA!!!");
		
		printf("\nInforme o nome do arquivo a ser lido: ");
		scanf("%s",nome_in);
				
		arq_ler = fopen(nome_in,"rb");
	}
	printf("\n FORMATANDO O TEXTO E PREPARANDO O MESMO PARA LEITURA. \n(PODE DEMORAR UM POUCO) \n");
	
	//informa ao usuario que o aplicativo em questao esta vazio	
	if(arq_ler == NULL)
	{
		printf("\n\n Arquivo vazio ");
		return;
	}
	
	while(!feof(arq_ler))
	{
		fscanf(arq_ler,"%c",&letra);
		
		if(i != 0)
		{
			aux->proxima = add_letras(letra, aux);
			aux = aux->proxima;
		}else
		{
			inicio_lista_letras = add_letras(letra,NULL);
			aux = inicio_lista_letras;
			i++;
		}
	}
	
	retirar_letras(nome_out);
}

void limpar_dados2(struct _LETRAS_ *lista)
{
	struct _LETRAS_ *atual, *prox;
	
	if(lista == NULL)
	{
		return;
	}
	
	atual = lista->proxima;
	
	while(atual != NULL)
	{
		prox = atual->proxima;
		free(atual);
		atual = prox;
	}
}

letras add_letras(char letra, letras anterior)
{
	letras L;
	L = malloc(sizeof(struct _LETRAS_));
	L->letra = letra;
	L->proxima = NULL;
	L->anterior = anterior;
	
	return L;
}
//FIM
