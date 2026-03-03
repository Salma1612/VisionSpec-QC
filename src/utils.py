
import matplotlib.pyplot as plt

def plot_training_history(history, save_path=None):

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']

    epochs = range(len(acc))

    plt.figure(figsize=(12, 5))

    # Accuracy Plot
    plt.subplot(1, 2, 1)
    plt.plot(epochs, acc)
    plt.plot(epochs, val_acc)
    plt.title('Training and Validation Accuracy')
    plt.legend(['Train Accuracy', 'Validation Accuracy'])

    # Loss Plot
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss)
    plt.plot(epochs, val_loss)
    plt.title('Training and Validation Loss')
    plt.legend(['Train Loss', 'Validation Loss'])

    if save_path:
        plt.savefig(save_path)

    plt.show()
