import cv2

def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return # early return

    # Configuração da fonte do texto
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.6
    cor_texto = (255, 255, 255)
    espessura = 1

    print("[ESPAÇO] Capturar e salvar foto")
    print("[ESCAPE] Sair")

    while True: # do-while
        status, frame = webcam.read()

        if not status:
            print("Falha ao receber o frame da webcam.")
            break

        frame_limpo = frame.copy()

        cv2.rectangle(frame, (10, 10), (320, 75), (0, 0, 0), -1)
        cv2.putText(frame, "[ESPAÇO] Salvar foto", (20, 35), fonte, escala, cor_texto, espessura)
        cv2.putText(frame, "[ESCAPE] Sair", (20, 60), fonte, escala, cor_texto, espessura)

        cv2.imshow("Captura da  Webcam local", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == 32:
            cv2.imwrite("foto.jpg", frame_limpo)
            print("Foto salva: foto.jpg")

            foto_cinza = cv2.cvtColor(frame_limpo, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("foto_cinza.jpg", foto_cinza)

            foto_invertida = cv2.cvtColor(frame_limpo, cv2.COLOR_RGB2BGR)
            cv2.imwrite("foto_invertida.jpg", foto_invertida)
            
            foto_legal = cv2.cvtColor(frame_limpo, cv2.COLORMAP_TURBO)
            cv2.imwrite("foto_legal.jpg", foto_legal)
            
            

        elif tecla == 27:
            print("Encerramento câmera...")
            break

    webcam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capturar_e_salvar()